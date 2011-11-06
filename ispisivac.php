<?php
include_once "/XMLklase/baza_ovisnosti.php";

class ispisivac extends baza_ovisnosti{
    private $stringovi = array();
   
    
    public function pokupi_string($string){
        $this->stringovi[] = $string; 
    }
    public function pokupi_ovisnosti($js_ovisnosti,$css_ovisnosti){
        $this->dodaj_ovisnost($js_ovisnosti,"js_ovisnost");
        $this->dodaj_ovisnost($css_ovisnosti,"css_ovisnost");
        
    }
   
    
    public function ispisi_body(){
        foreach($this->stringovi as $string){
            echo $string;
        }
    }
    
    public function napravi_stranicu(){
        
        $root =konstante::lokacije("domena")."/".konstante::lokacije("root_folder");
        
        echo "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">
                <html><head>";
        echo "<script type=\"text/javascript\" src=\"".$root."/jquery-1.6.1.js\"></script>";
        
        foreach($this->js_ovisnost as $ovisnost){
            echo "<script type=\"text/javascript\" src=\"".$root."/".konstante::lokacije("javascript")."/".$ovisnost."\"></script>";
        }
        foreach($this->css_ovisnost as $ovisnost){
            echo "<link rel=\"stylesheet\" type=\"text/css\" href=\"".$root."/".konstante::lokacije("css")."/".$ovisnost."\"/>";
        }
        echo "</head><body>";
        $this->ispisi_body();
    
        echo "</body></html>";
        
    }
    
}



?>