# Configure mouse speed

마우스 아이디를 확인한다.

    xinput --list --short

마우스 속도를 조절한다. `9`는 아이디 `2`는 원하는 값.

    xinput -set-prop 9 'Device Accel Constant Deceleration' 2
