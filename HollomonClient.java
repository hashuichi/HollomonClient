import java.net.*;
import java.io.*;
import java.util.*;

public class HollomonClient {
    private String server;
    private int port;
    private Socket socket;
    private BufferedWriter out;
    private CardInputStream in;
    
    public HollomonClient(String server, int port){
        this.server = server;
        this.port = port;
        try {
            this.socket = new Socket(this.server, this.port); 
            this.out = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
            this.in = new CardInputStream(socket.getInputStream());
        } catch (IOException e) {
            System.err.println("Error: "+e);
        }
    }

    public List<Card> obtainCards() throws IOException{
        List<Card> list = new ArrayList<Card>();
        Card card = in.readCard();
        while (card != null) {
            list.add(card);
            card = in.readCard();
        }
        Collections.sort(list);
        return list;
    }

    public List<Card> login(String username, String password){
        try {           
            out.write(username);
            out.write("\n");
            out.write(password);
            out.write("\n");
            out.flush();
            if (in.readResponse().contains(username)){
                return obtainCards();
            }
        } catch(Exception e) {
            System.err.println("Error:"+e);
        }
        return null;
    }

    public long getCredits() throws IOException{
        out.write("CREDITS");
        out.write("\n");
        out.flush();
        Long result = new Long(in.readResponse());
        // Clear out the OK message 
        in.readResponse();
        return result;
    }

    public List<Card> getCards() throws IOException{
        out.write("CARDS");
        out.write("\n");
        out.flush();
        return obtainCards();
    }

    public List<Card> getOffers() throws IOException{
        out.write("OFFERS");
        out.write("\n");
        out.flush();
        return obtainCards();
    }
    
    public boolean buyCard(Card card) throws IOException{
        if (getCredits() >= card.getPrice()){
            out.write("BUY "+card.getID());
            out.write("\n");
            out.flush();
            if (in.readResponse().contains("OK")){
                return true;
            }
        }
        return false;
    }

    public boolean sellCard(Card card, long price) throws IOException{
        out.write("SELL "+card.getID()+" "+price);
        out.write("\n");
        out.flush();
        if (in.readResponse().contains("OK")){
            return true;
        }
        return false;
    }

    public void close() throws IOException{
        in.close();
        out.close();
    }
}