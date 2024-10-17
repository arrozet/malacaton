package UBICACION;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class Principal {
    public static void main(String[] args) {
        String urlString = "https://g4feb4b88427ce8-malackaton.adb.eu-marseille-1.oraclecloudapps.com/ords/admin/agua/";
        String filter = "$filter=ID gt 3";  // Filtro para IDs mayores que 3
        String urlWithParams = urlString + "?" + filter;  // Concatenar la URL con el filtro

        try {
            // Crear la URL
            URL url = new URL(urlWithParams);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            conn.setRequestProperty("Content-Type", "application/json");
            conn.setRequestProperty("Authorization", "Bearer your_access_token"); // Reemplaza con tu token de acceso

            // Verificar la respuesta
            int responseCode = conn.getResponseCode();
            if (responseCode == HttpURLConnection.HTTP_OK) { // Código 200
                BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
                String inputLine;
                StringBuilder response = new StringBuilder();

                while ((inputLine = in.readLine()) != null) {
                    response.append(inputLine);
                }
                in.close();

                // Mostrar el resultado
                System.out.println("Response: " + response.toString());
            } else {
                System.out.println("Error: " + responseCode);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

