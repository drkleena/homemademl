table_md = "|$\text{P}(\text{Flu})=\frac{3}{5}$                                         |$\text{P}(\text{Cold})=\frac{2}{5}$||\
|$\text{P}(\text{Headache} = \textit{severe } | \text{ Flu})=\frac{2}{3}$   |$\text{P}(\text{Headache} = \textit{severe } | \text{ Cold})=\frac{0}{2}$||\
|$\text{P}(\text{Headache} = \textit{mild } | \text{ Flu})=\frac{1}{3}$     |$\text{P}(\text{Headache} = \textit{mild } | \text{ Cold})=\frac{1}{2}$||\
|$\text{P}(\text{Headache} = \textit{no } | \text{ Flu})=\frac{0}{3}$       |$\text{P}(\text{Headache} = \textit{no } | \text{ Cold})=\frac{1}{2}$||\
|$\text{P}(\text{Sore} = \textit{severe } | \text{ Flu})=\frac{1}{3}$       |$\text{P}(\text{Sore} = \textit{severe } | \text{ Cold})=\frac{1}{2}$||\
|$\text{P}(\text{Sore} = \textit{mild } | \text{ Flu})=\frac{2}{3}$         |$\text{P}(\text{Sore} = \textit{mild } | \text{ Cold})=\frac{0}{2}$||\
|$\text{P}(\text{Sore} = \textit{no } | \text{ Flu})=\frac{0}{3}$           |$\text{P}(\text{Sore} = \textit{no } | \text{ Cold})=\frac{1}{2}$||\
|$\text{P}(\text{Temperature} = \textit{high } | \text{ Flu})=\frac{1}{3}$  |$\text{P}(\text{Temperature} = \textit{high } | \text{ Cold})=\frac{0}{2}$||\
|$\text{P}(\text{Temperature} = \textit{normal } | \text{ Flu})=\frac{2}{3}$|$\text{P}(\text{Temperature} = \textit{normal } | \text{ Cold})=\frac{2}{2}$||\
|$\text{P}(\text{Cough} = \textit{yes } | \text{ Flu})=\frac{3}{3}$         |$\text{P}(\text{Cough} = \textit{yes } | \text{ Cold})=\frac{1}{2}$||\
|$\text{P}(\text{Cough} = \textit{no } | \text{ Flu})=\frac{0}{3}$          |$\text{P}(\text{Cough} = \textit{no } | \text{ Cold})=\frac{1}{2}$||"

table_md = table_md.replace("\t", "\\t")
table_md = table_md.replace("\f", "\\f")
table_md = table_md.strip()
table_md = table_md.replace(" ", "")

table_md = table_md.split("||")
html_row = "<div class=\"table-row\">$$$$</div>"
html_row_item = "<div class=\"table-data\">$$$$</div>"

for row in table_md:

    items = row.split("$");
    items = list(filter(lambda a: (a!='|'), items))
    items = list(filter(lambda a: (a!=''), items))


    for item in items:

        item_html_string = html_row_item.replace("$$$$", str("$$"+item+"$$")))
        
