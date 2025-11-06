import time

class AHT20:
    def __init__(self, i2c, addr=0x38):
        self.i2c = i2c
        self.addr = addr
        # Wake/init is usually not required on AHT20, but a short delay helps after power-up
        time.sleep_ms(50)

    def _measure(self):
        # Trigger measurement: 0xAC, 0x33, 0x00 (per AHT20 datasheet)
        self.i2c.writeto(self.addr, b'\xAC\x33\x00')
        # Busy bit is bit7 of status byte. Poll until clear.
        for _ in range(100):
            time.sleep_ms(10)
            status = self.i2c.readfrom(self.addr, 1)[0]
            if (status & 0x80) == 0:  # not busy
                break
        # Read 6 bytes: [status, Hh, Hm, Hl/Tt, Tm, Tl]
        data = self.i2c.readfrom(self.addr, 6)
        return data

    def read(self):
        d = self._measure()
        # 20-bit humidity: bits [19:0] across bytes 1..3 (top 4 bits of byte3 belong to H)
        raw_h = (d[1] << 12) | (d[2] << 4) | (d[3] >> 4)
        # 20-bit temperature: low 4 bits of byte3 + bytes 4..5
        raw_t = ((d[3] & 0x0F) << 16) | (d[4] << 8) | d[5]
        rh = raw_h / 1048576.0 * 100.0
        tc = raw_t / 1048576.0 * 200.0 - 50.0
        return tc, rh

    @property
    def temperature(self):
        return self.read()[0]

    @property
    def humidity(self):
        return self.read()[1]