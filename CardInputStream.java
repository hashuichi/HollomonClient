import java.io.*;

public class CardInputStream extends InputStream {
    private BufferedReader input;

    public CardInputStream(InputStream input){
        this.input = new BufferedReader(new InputStreamReader(input));
    }

    @Override
    public void close() throws IOException{
        this.input.close();
    }

    public Card readCard() throws IOException {
        if (input.readLine().contains("CARD")) {
            long id = new Long(input.readLine());
            String name = input.readLine();
            Rank rank = Rank.valueOf(input.readLine());
            long price = new Long(input.readLine());
            Card card = new Card(id, name, rank, price);
            return card;
        }
        return null;
    }

    public String readResponse() throws IOException {
        return input.readLine();
    }

    @Override 
    public int read() throws IOException {
        return input.read();
    }


}