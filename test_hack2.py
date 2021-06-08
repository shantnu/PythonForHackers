from hack2 import heart_bleed,stack_overflow,buffer_overflow

def dontusetest_stack_overflow():
    import pdb;pdb.set_trace()
    counter = stack_overflow()
    assert counter == 11

def test_heartbleed():
    msg = heart_bleed(test_mode = True)
    assert "This is a secret string. You should not be able to read this" in str(msg).replace("\\n", "")

def test_buffer_overflow():
    text,counter=buffer_overflow()
    assert "This is the secret file. You should not be able to read it" in str(text)