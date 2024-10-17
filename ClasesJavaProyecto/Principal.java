import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class Principal {
    public static void main(String[] args) {
        // URL de tu API de embalses
        String urlString = "https://g4feb4b88427ce8-malackaton.adb.eu-marseille-1.oraclecloudapps.com/ords/admin/embalses/";
        
        try {
            // Crear la URL
            URL url = new URL(urlString);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET"); // Método GET
            conn.setRequestProperty("Content-Type", "application/json"); // Indicamos que esperamos JSON
            
            // Si tu API necesita autenticación (Bearer Token), añade el siguiente encabezado
            // conn.setRequestProperty("Authorization", "Bearer your_access_token");

            // Verificar la respuesta
            int responseCode = conn.getResponseCode();
            if (responseCode == HttpURLConnection.HTTP_OK) { // Código 200 OK
                BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
                String inputLine;
                StringBuilder response = new StringBuilder();

                // Leer la respuesta
                while ((inputLine = in.readLine()) != null) {
                    response.append(inputLine);
                }
                in.close();

                // Mostrar la respuesta
                System.out.println("Response: " + response.toString());
            } else {
                System.out.println("Error: " + responseCode);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

