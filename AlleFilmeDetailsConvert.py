    # Funktion zum Einlesen der Datei und Umwandeln in HTML
    def convert_to_html(input_file, output_file):
        # Einträge speichern
        entries = []
        
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            # Einträge durch doppelte Zeilenumbrüche trennen
            entries = content.split('\n\n')

        # Sortieren, aber führendes "[" ignorieren
        entries = sorted(
            entries,
            key=lambda x: x[1:] if x[0].startswith("[") else x)

        # HTML-Dokument erstellen
        html_content = '<html>\n<head>\n<title>Filme</title>\n</head>\n<body>\n'
        html_content += '<h1>Filme</h1>\n'

        count = 0
        for entry in entries:
            lines = entry.split('\n')
            if len(lines) != 8:
                print("----")
                print("\n".join(lines))
                continue  # Falls nicht genug Informationen vorhanden sind

            title = lines[0].strip() 
            iso   = lines[1].strip() 
            imdb  = lines[2].strip() 
            year  = lines[3].strip() 
            mins  = lines[4].strip() 
            cat   = lines[5].strip() 
            act   = lines[6].strip() 
            desc  = lines[7].strip() 

            for letter in iso:
                if letter not in ".-":
                    folder = letter
                    break
            
            # HTML-Block für jeden Film
            html_content +=  '<hr>\n'  # Horizontale Linie vor jedem Film
            #html_content += f'<img src={img} style="max-width: 150px; height: auto;">\n'
            html_content += f'<div class="film-entry">\n'
            html_content += f'  <h2>\n'
            html_content += f'    <a href="{imdb}" target="_blank">{title}</a> ({year})\n'
            html_content += f'  </h2>\n'
            html_content += f'  <p>'
            html_content += f'  </p>\n'
            html_content += f'  <p><strong>{cat}</strong> ({mins} Min.)</p>\n'
            html_content += f'  <p><em>Mit {act}</em></p>\n'
            html_content += f'  <p>{desc}</p>\n'
            html_content +=  '</div>\n'

        html_content += '</body>\n</html>'

        # HTML in eine Datei schreiben
        with open(output_file, 'w', encoding='utf-8') as out_file:
            out_file.write(html_content)

    # Benutzereingaben
    folder = 'C:\\Users\\Herbert\\Documents\\'
    input_file  = folder + 'AlleFilmeDetails.txt'  # Der Name der Eingabedatei
    output_file = folder + 'AlleFilmeDetails.html' # Der Name der Ausgabedatei

    # Umwandeln der Datei
    convert_to_html(input_file, output_file)
    #return
