from unittest import TestCase

import RFXtrx


class BbqTestCase(TestCase):

    def setUp(self):
        self.parser = RFXtrx.lowlevel.Bbq()

    def test_parse_bytes(self):
        self.data = bytearray([0x0a, 0x4e, 0x01, 0x06, 0xfc, 0xd8, 0x00, 0x13, 0x00, 0x13, 0x79])
        bbq = RFXtrx.lowlevel.parse(self.data)
        self.assertEquals(RFXtrx.lowlevel.Bbq, type(bbq))
        self.assertEquals(bbq.temp1,19)
        self.assertEquals(bbq.temp2,19)
        self.assertEquals(bbq.type_string,'BBQ1 - Maverick ET-732')
        self.assertEquals(bbq.id_string,'fcd800:78')                

