<?php

if(isset($_POST['genimgnum'])) {
    $genimgnum = $_POST['genimgnum'];
    // OS command injection
    exec("python3 ../python/make_test_license_plates.py " . $genimgnum);

    $pathimgs = "./imgs/";
    $dirlist = array_diff(scandir($pathimgs), array('.', '..'));

    $filelist = [];
    foreach ($dirlist as $key => $value) {
        $path = $pathimgs . $value;
        //$filelist[] = array_diff(scandir($path), array('.', '..'));
        $filelist[$value] = array_diff(scandir($path), array('.', '..'));
    }
    $filelist = json_encode($filelist, JSON_PRETTY_PRINT);
    echo($filelist);
}

if(isset($_POST['predictimg'])) {
    $predictimgname = $_POST['predictimg'];
    // OS command injection
    echo(exec("python3 ../python/predict_number.py " . $predictimgname));
}

?>
