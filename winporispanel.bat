echo off

if [%1]==[] (
    echo Must provide an argument!
) else (
    del models\%1.ods
    del models\%1.xml
    copy .\config_csys_disabled.py .\config_csys.py

    python graph2poris.py models\%1.graphml
    if exist .\models\%1.ods (
        python poris2xml.py models\%1.ods
        if exist .\models\%1.xml (
            java -jar AstroPorisPlayer\bin\AstroPorisPlayer.jar models\%1.xml
        ) else (
            echo "graph2poris could not be processed"
            echo A second statement
        ) 
    ) else (
        echo "poris2xml could not be processed"
        echo A second statement
    ) 
)

