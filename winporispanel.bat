echo off

if [%1]==[] (
    echo Must provide an argument!
) else (
    set DEVNAME=%1
    set OUTPUT_PORIS_DIR=output\py\%1\%1
    set OUTPUT_ODS_DIR=output\ods
    set OUTPUT_XML_DIR=output\xml
    set OUTPUT_MODEL_FILE=%OUTPUT_PORIS_DIR%\%1PORIS.py
    set OUTPUT_XML_FILE=%OUTPUT_XML_DIR%\%1.xml

    del %OUTPUT_ODS_DIR%\%1.ods
    del %OUTPUT_XML_FILE%
    del %OUTPUT_XML_DIR%\%1.from-python.xml
    mkdir %OUTPUT_PORIS_DIR%
    mkdir %OUTPUT_ODS_DIR%
    mkdir %OUTPUT_XML_DIR%
    copy .\config_csys_disabled.py .\config_csys.py

    python graph2poris.py models\%1.graphml --output-dir %OUTPUT_PORIS_DIR% --ods-output-dir %OUTPUT_ODS_DIR%
    if exist %OUTPUT_MODEL_FILE% (
        python poris_python2xml.py %OUTPUT_MODEL_FILE% --output %OUTPUT_XML_FILE%
        if exist %OUTPUT_XML_FILE% (
            java -jar AstroPorisPlayer\bin\AstroPorisPlayer.jar %OUTPUT_XML_FILE%
        ) else (
            echo "poris_python2xml could not be processed"
        )
    ) else (
        echo "graph2poris could not be processed"
    )
)
