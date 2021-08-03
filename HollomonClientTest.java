import java.util.*;
import java.io.*;

public class HollomonClientTest {
    public static void main(String[] args){
        try {
            HollomonClient hc = new HollomonClient("netsrv.cim.rhul.ac.uk", 1812);
            List n = hc.login("truth", "hestrongmission");
            System.out.println(n);
            System.out.println(hc.getCredits()+"\n"+hc.getCards()+"\n"+hc.getOffers());
            hc.close();
        } catch(IOException e) {}
    }
}