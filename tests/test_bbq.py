from unittest import TestCase

import RFXtrx


class TempHumidityTestCase(TestCase):

    def setUp(self):
        self.parser = RFXtrx.lowlevel.Bbq()

    def test_parse_bytes(self):
        self.data = bytearray([0x0a 0x4e 0x01 0x06 0xfc 0xd8 0x00 0x13 0x00 0x13 0x79])
        bbq = RFXtrx.lowlevel.parse(self.data)
        self.assertEquals(RFXtrx.lowlevel.Bbq, type(bbq))
        self.assertEquals(temphum.temp1,16.7)
        self.assertEquals(temphum.temp2,45)
        self.assertEquals(temphum.type_string,'THGR810, THGN800')
        self.assertEquals(temphum.id_string,'70:02')                

