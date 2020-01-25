<?php
if(isset($_POST['Pole1'])){
    $Name = 'Pole1';
    $Pole   = addslashes( trim($_POST['Pole1']) );
  
  }else if(isset($_POST['Pole2'])){
    $Name = 'Pole2';
    $Pole   = addslashes( trim($_POST['Pole2']) );
  
  }else if(isset($_POST['Pole3'])){
    $Name = 'Pole3';
    $Pole   = addslashes( trim($_POST['Pole3']) );
  
  }else if(isset($_POST['Pole4'])){
    $Name = 'Pole4';
    $Pole   = addslashes( trim($_POST['Pole4']) );
  
  }
  
  if(isset($Name)){
    mysql_pconnect("std-mysql.ist.mospolytech.ru","std_866","qwertyuio") or die ("Невозможно подключение к MySQL");
    mysql_select_db("test") or die ("Невозможно открыть таблицу с данными");
  
    $result = mysql_query ("INSERT INTO dannye ('".$Name."') VALUES ('".$Pole."')");
    if ($result)
      echo 'Ты нажал на кнопку '.$Pole.' теперь в базе, в этом поле, сможешь найти запись, со значением "'.$Pole.'"';
    mysql_close ($connect);
  }
?>