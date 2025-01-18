#include <SFML/Graphics.hpp>
#include <SFML/Window.hpp>
#include <iostream>
#include <string>

int main() {
    // Crear ventana
    sf::RenderWindow window(sf::VideoMode(300, 400), "Calculadora");

    // Fuente para texto
    sf::Font font;
    font.loadFromFile("arial.ttf");

    // Texto para entrada
    sf::Text entrada;
    entrada.setFont(font);
    entrada.setCharacterSize(24);
    entrada.setFillColor(sf::Color::Black);
    entrada.setPosition(20, 20);

    // Botones
    sf::RectangleShape botones[16];
    for (int i = 0; i < 16; i++) {
        botones[i].setSize(sf::Vector2f(60, 60));
        botones[i].setFillColor(sf::Color::White);
        botones[i].setOutlineColor(sf::Color::Black);
        botones[i].setOutlineThickness(1);
    }

    // Posiciones de botones
    int row = 0;
    int col = 0;
    for (int i = 0; i < 16; i++) {
        botones[i].setPosition(20 + col * 70, 100 + row * 70);
        col++;
        if (col > 3) {
            col = 0;
            row++;
        }
    }

    // Texto para botones
    sf::Text textoBotones[16];
    for (int i = 0; i < 16; i++) {
        textoBotones[i].setFont(font);
        textoBotones[i].setCharacterSize(24);
        textoBotones[i].setFillColor(sf::Color::Black);
    }

    // Asignar texto a botones
    std::string texto[16] = {"7", "8", "9", "/",
                                "4", "5", "6", "*",
                                "1", "2", "3", "-",
                                "0", ".", "=", "+"};
    for (int i = 0; i < 16; i++) {
        textoBotones[i].setString(texto[i]);
        textoBotones[i].setPosition(botones[i].getPosition().x + 20, botones[i].getPosition().y + 15);
    }

    // Variable para almacenar entrada
    std::string entradaTexto = "";

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();

            if (event.type == sf::Event::MouseButtonPressed) {
                for (int i = 0; i < 16; i++) {
                    if (botones[i].getGlobalBounds().contains(event.mouseButton.x, event.mouseButton.y)) {
                        if (i < 15) {
                            entradaTexto += texto[i];
                            entrada.setString(entradaTexto);
                        } else {
                            // Calcular resultado
                            try {
                                double resultado = std::stod(entradaTexto);
                                entradaTexto = std::to_string(resultado);
                                entrada.setString(entradaTexto);
                            } catch (std::exception& e) {
                                entradaTexto = "Error";
                                entrada.setString(entradaTexto);
                            }
                        }
                    }
                }
            }
        }

        window.clear();
        window.draw(entrada);

        for (int i = 0; i < 16; i++) {
            window.draw(botones[i]);
            window.draw(textoBotones[i]);
        }

        window.display();
    }

    return 0;
}