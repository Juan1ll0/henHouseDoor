import machine

# Standby device. Decrease power consumption.
def DeepSleep(msecs):
  print("zzzzzz.....")
  rtc = machine.RTC()
  rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
  rtc.alarm(rtc.ALARM0, msecs)
  machine.deepsleep()