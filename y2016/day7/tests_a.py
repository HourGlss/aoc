from y2016.day7.main_a import IP
from y2016.day7.data import test_input,test_input_b

def test_create_IP():
    data = "abba[mnop]qrst"
    ip = IP(data)
    assert ip.hypernets ==['mnop']
    assert ip.outsides == ['abba','qrst']

def test_IP_tls_tests():
    raw_inputs = test_input.split('\n')
    ip = IP(raw_inputs[0])
    assert ip.supports_tls()
    ip = IP(raw_inputs[1])
    assert not ip.supports_tls()
    ip = IP(raw_inputs[2])
    assert not ip.supports_tls()
    ip = IP(raw_inputs[3])
    assert ip.supports_tls()







