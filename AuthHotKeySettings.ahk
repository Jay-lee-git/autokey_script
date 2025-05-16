!b::
Send, ^k
Sleep, 100
Send, ^v
Sleep, 100
Send, {Enter}
return

CapsLock::Ctrl
Ctrl::CapsLock
;오토핫키 홈페이지 https://www.autohotkey.com/docs/Hotkeys.htm 
; ctrl = ^ 
; alt = !
; shift =  +

; **** alt c -> {Click}****
^!`:: Send {Enter}
;************** alt 활용 방향키 **************


;===== 방향키 이동 ======

!j:: Send {Down}
!k:: Send {Up}
!h:: Send {Left}
!l:: Send {Right}
!u:: Send {Home}
!i:: Send {End}
!p:: Send {PgUp}
!;:: Send {PgDn}

!s:: Send {Down}
!w:: Send {Up}
!a:: Send {Left}
!d:: Send {Right}




; alt + ctrl
^!h:: Send ^{Left}
^!l:: Send ^{Right}
^!j:: Send !^{Down}
^!k:: Send !^{Up}


; alt + ctrl + shift
+^!k:: Send !{Up}
+^!j:: Send !{Down}
+^!h:: Send ^+{Left}
+^!l:: Send ^+{Right}


; shift + alt
+!j:: Send +{Down}
+!k:: Send +{Up}
+!h:: Send +{Left}
+!l:: Send +{Right}
+!u:: Send +{Home}
+!i:: Send +{End}
+!p:: Send +{PgUp}
+!;:: Send +{PgDn}




;************** 기타 편의성 방향키 추가 **************



; **** alt q -> Backspace ****
!q::Send {BackSpace}

; **** alt e -> Delete****
!e::Send {Delete} 

;**** 바탕화면으로 가기 단축키 해제 ****
#d::return
;**** 받아쓰기 단축키 해제 ****
#h::return

;**** 캡스락 한영변경, 실제 캡스락 기능은 shift+caps로 변경 **** 
^Space::Send, {vk15sc138}