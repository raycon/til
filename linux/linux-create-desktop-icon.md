# Create desktop icon

`~/.local/share/applications` 경로에 `filename.desktop`으로 다음과 같이 파일을 만든다.

    [Desktop Entry]
    Name=Eclipse
    Type=Application
    Exec=/opt/eclipse/eclipse
    Terminal=false
    Icon=/opt/eclipse/icon.xpm
    Comment=Eclipse IDE
    NoDisplay=false
    Categories=Development;IDE;
    Name[en]=Eclipse

다음 명령어로 실행 권한을 추가한다

    chmod +x filename.desktop