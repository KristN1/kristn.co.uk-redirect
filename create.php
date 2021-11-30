<?php

const create_url = "http://localhost:5000/create";
$url = ($_POST["url"]);

echo url;

$opts = array("http" =>
array(
    "method" => "POST",
    "header" => "url: " + $_POST["url"],
    )
);

$context = stream_context_create($opts);
$result = file_get_contents(create_url, false, $context);
echo $result;


?>