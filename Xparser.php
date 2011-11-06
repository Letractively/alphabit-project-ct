<?php
include_once "/utility/file_citac.php";
function __autoload($ime){
    include "/XMLklase/".$ime.".php";
    }


class Xparser{
    private $stack = array();
    private $parser;
    private $datoteka;
    private $brojac_djece;
    private $root_id;
    private $mod;
    
    //truba staviti i mod tako da se za da li se parsira struktura ili dijelovi sadrzaja/prkaza/sucelja za unos
    public function __construct($file,$mod=null){
        
        // "f" - file, null-plain xml, 
        $this->mod = $mod;
        $this->datoteka=$file;
        $this->parser=xml_parser_create('');
        xml_parser_set_option($this->parser,XML_OPTION_SKIP_WHITE,TRUE);
        xml_parser_set_option($this->parser,XML_OPTION_CASE_FOLDING,FALSE);
        xml_set_object($this->parser,$this);
        xml_set_element_handler($this->parser,"staviObjektNaStack","zapakirajObjektURoditelja");
        xml_set_character_data_handler($this->parser,"zapakirajSadrzajURoditelja");
        
        
    }
    
    //ovo potencijalno triba popravit  
    
    
    public function parsiraj($id="r"){
        $this->root_id=$id;
        
        
        
        
        if($this->mod =="f"){
            $citac = new file_citac($this->datoteka);
            $dokument = $citac->procitaj();
        }else{
            $dokument = $this->datoteka;
        }
        //file
        /*
        if(!$fp=fopen($this->datoteka,"rb")){
            throw new Exception("nemogu otvoriti datoteku: ".$this->datoteka);
        }
        $dokument=fread($fp,filesize($this->datoteka));
        fclose($fp);
        */
        
        
        
        
        //$dokument=file_get_contents($this->datoteka);
        if(xml_parse($this->parser,$dokument)){
            //echo "uspio sam<br/>";
        }else{
            echo xml_error_string(xml_get_error_code($this->parser));
        }
        xml_parser_free($this->parser);
        
        return $this->stack[0];
    }
    
    private function staviObjektNaStack($parser,$ime,array $atributi){
        
        $atributi["id"]=$this->dodijeli_id();
        
        $objekt=new $ime($atributi);
        
        $this->stack[]=&$objekt;
        
        //$this->dodijeli_id($objekt);
        //echo $objekt->id()."--".get_class($objekt)."<br />";
        
    }
    private function zapakirajObjektURoditelja($parser,$ime){
        //echo "pozvao me ime ".$ime;
        if(!is_a(end($this->stack),$ime)){
            throw new Exception("oso stack k vragu!!!!! - zatvoreni tag ne odgovara zandnjem elementu na stacku");
        }
        
        $trenutni = end($this->stack);
       
        if($prvi_roditelj=$this->prvi_roditelj()){
            
            $trenutni->dodijeli_roditelja($prvi_roditelj);
                                   
            $prvi_roditelj->dodajDite($trenutni);
            
            
            //$this->stack[$broj_elemenata-1]->roditelj=$this->stack[$broj_elemenata-2];
            //$this->stack[$broj_elemenata-2]->dodajDite($this->stack[$broj_elemenata-1]);
            
            array_pop($this->stack);
        }
    }
    
    private function zapakirajSadrzajURoditelja($parser,$podatci){
        
        $broj_elemenata =sizeof($this->stack);
        $podatci=trim($podatci);
        if($podatci){
        $this->stack[$broj_elemenata-1]->dodajDite(trim($podatci));
        }
    }
    
    private function dodijeli_id(){
        
        $roditelj=end($this->stack);
        if($roditelj){
            
            $id = $roditelj->id()."_".($roditelj->broj_dice()+1);     
        }else{
            $id = $this->root_id;
        }
        return $id;
    }
    
    // vraæa buduæeg roditelja na stacku dakle 2 clan s desna
    private function prvi_roditelj(){
        $broj_elemenata = sizeof($this->stack);
        if($broj_elemenata>1){
            return $this->stack[$broj_elemenata-2];
        }else{
            return false;
        }
    }
    

}



?>
    