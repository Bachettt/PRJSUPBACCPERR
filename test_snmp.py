from pysnmp.hlapi import *

errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData('public'),  # Remplacez 'public' par le nom de la communauté SNMP si différent
           UdpTransportTarget(('192.168.141.58', 161)),  # IP de la machine cible
           ContextData(),
           ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))
)

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))





  File "C:\ProgramData\Anaconda3\lib\site-packages\pysnmp\carrier\asyncore\dispatch.py", line 45, in runDispatcher
    loop(timeout or self.getTimerResolution(),

  File "C:\ProgramData\Anaconda3\lib\asyncore.py", line 207, in loop
    poll_fun(timeout, map)

  File "C:\ProgramData\Anaconda3\lib\asyncore.py", line 150, in poll
    read(obj)

  File "C:\ProgramData\Anaconda3\lib\asyncore.py", line 87, in read
    obj.handle_error()

  File "C:\ProgramData\Anaconda3\lib\asyncore.py", line 83, in read
    obj.handle_read_event()

  File "C:\ProgramData\Anaconda3\lib\asyncore.py", line 420, in handle_read_event
    self.handle_read()

  File "C:\ProgramData\Anaconda3\lib\site-packages\pysnmp\carrier\asyncore\dgram\base.py", line 170, in handle_read
    self._cbFun(self, transportAddress, incomingMessage)

  File "C:\ProgramData\Anaconda3\lib\site-packages\pysnmp\carrier\base.py", line 84, in _cbFun
    self.__recvCallables[recvId](

  File "C:\ProgramData\Anaconda3\lib\site-packages\pysnmp\entity\engine.py", line 151, in __receiveMessageCbFun
    self.msgAndPduDsp.receiveMessage(

  File "C:\ProgramData\Anaconda3\lib\site-packages\pysnmp\proto\rfc3412.py", line 291, in receiveMessage
    msgVersion = verdec.decodeMessageVersion(wholeMsg)

  File "C:\ProgramData\Anaconda3\lib\site-packages\pysnmp\proto\api\verdec.py", line 15, in decodeMessageVersion
    seq, wholeMsg = decoder.decode(

  File "C:\ProgramData\Anaconda3\lib\site-packages\pyasn1\codec\ber\decoder.py", line 2003, in __call__
    for asn1Object in streamingDecoder:

  File "C:\ProgramData\Anaconda3\lib\site-packages\pyasn1\codec\ber\decoder.py", line 1918, in __iter__
    for asn1Object in self._singleItemDecoder(

  File "C:\ProgramData\Anaconda3\lib\site-packages\pyasn1\codec\ber\decoder.py", line 1778, in __call__
    for value in concreteDecoder.valueDecoder(

  File "C:\ProgramData\Anaconda3\lib\site-packages\pyasn1\codec\ber\decoder.py", line 654, in valueDecoder
    for chunk in substrateFun(asn1Object, substrate, length, options):

TypeError: <lambda>() takes 3 positional arguments but 4 were given


During handling of the above exception, another exception occurred:

Traceback (most recent call last):

  File "D:\Users\user\Downloads\test_snmp1.py", line 3, in <module>
    errorIndication, errorStatus, errorIndex, varBinds = next(

  File "C:\ProgramData\Anaconda3\lib\site-packages\pysnmp\hlapi\asyncore\sync\cmdgen.py", line 113, in getCmd
    snmpEngine.transportDispatcher.runDispatcher()

  File "C:\ProgramData\Anaconda3\lib\site-packages\pysnmp\carrier\asyncore\dispatch.py", line 50, in runDispatcher
    raise PySnmpError('poll error: %s' % ';'.join(format_exception(*exc_info())))

PySnmpError: poll error: Traceback (most recent call last):
;  File "C:\ProgramData\Anaconda3\lib\site-packages\pysnmp\carrier\asyncore\dispatch.py", line 45, in runDispatcher
    loop(timeout or self.getTimerResolution(),
;  File "C:\ProgramData\Anaconda3\lib\asyncore.py", line 207, in loop
    poll_fun(timeout, map)
;  File "C:\ProgramData\Anaconda3\lib\asyncore.py", line 150, in poll
    read(obj)
;  File "C:\ProgramData\Anaconda3\lib\asyncore.py", line 87, in read
    obj.handle_error()
;  File "C:\ProgramData\Anaconda3\lib\asyncore.py", line 83, in read
    obj.handle_read_event()
;  File "C:\ProgramData\Anaconda3\lib\asyncore.py", line 420, in handle_read_event
    self.handle_read()
;  File "C:\ProgramData\Anaconda3\lib\site-packages\pysnmp\carrier\asyncore\dgram\base.py", line 170, in handle_read
    self._cbFun(self, transportAddress, incomingMessage)
;  File "C:\ProgramData\Anaconda3\lib\site-packages\pysnmp\carrier\base.py", line 84, in _cbFun
    self.__recvCallables[recvId](
;  File "C:\ProgramData\Anaconda3\lib\site-packages\pysnmp\entity\engine.py", line 151, in __receiveMessageCbFun
    self.msgAndPduDsp.receiveMessage(
;  File "C:\ProgramData\Anaconda3\lib\site-packages\pysnmp\proto\rfc3412.py", line 291, in receiveMessage
    msgVersion = verdec.decodeMessageVersion(wholeMsg)
;  File "C:\ProgramData\Anaconda3\lib\site-packages\pysnmp\proto\api\verdec.py", line 15, in decodeMessageVersion
    seq, wholeMsg = decoder.decode(
;  File "C:\ProgramData\Anaconda3\lib\site-packages\pyasn1\codec\ber\decoder.py", line 2003, in __call__
    for asn1Object in streamingDecoder:
;  File "C:\ProgramData\Anaconda3\lib\site-packages\pyasn1\codec\ber\decoder.py", line 1918, in __iter__
    for asn1Object in self._singleItemDecoder(
;  File "C:\ProgramData\Anaconda3\lib\site-packages\pyasn1\codec\ber\decoder.py", line 1778, in __call__
    for value in concreteDecoder.valueDecoder(
;  File "C:\ProgramData\Anaconda3\lib\site-packages\pyasn1\codec\ber\decoder.py", line 654, in valueDecoder
    for chunk in substrateFun(asn1Object, substrate, length, options):
;TypeError: <lambda>() takes 3 positional arguments but 4 were given
caused by <class 'TypeError'>: <lambda>() takes 3 positional arguments but 4 were given