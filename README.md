## Citations

### db_connector.py
All code is based on the CS340 starter code unless otherwise noted.

### DDL.sql
All original work, no AI was used

### DML.sql
All original work, no AI was used

### PL.sql
Stored Procedures were adapted from provided OSU code in
modules. Update SPs were created with the assistance of AI
and documented where the source code is.
Other than that, all original work, no AI was used.

#### Specific citations for PL.sql
Line 279:
```
Date: 3/01/2026
Used example code for all DELETE stored procedures
Prompt used to generate stored procedure:
How do I turn this <Delete method in DML> into a stored procedure?
AI Source URL: https://claude.ai/
```

Line 381:
```
Date: 3/01/2026
Prompt used to generate stored procedure:
Used example code for all UPDATE stored procedures
How do I turn this <Update method in DML> into a stored procedure?
AI Source URL: https://claude.ai/
```

### app.py
All code is based on the CS340 starter code, with the exception of the actual queries
used for querying the DB or otherwise noted.

#### Specific citations for app.py
Line 42:
```
No AI tools used, but just google searched how to call stored procedures
using the MySQLdb library in python: cursor.callproc()
Date: 2/19/2026
```

Line 81:
```
Date: 2/19/2026
Prompts used to generate flask routes:
1. Help me write a flask app route to delete a plant from plant_in_bed using a stored procedure.
2. I need help writing a delete route for the plant-in-bed object (refactoring existing table and route code).
3. I need help troubleshooting MySQL Error 1305 (Procedure does not exist) and Error 2014 (Commands out of sync).
AI Source URL: https://gemini.google.com/
```

Line 158:
```
Citation for use of AI Tools:
Date: 2/19/2026
Prompts used to generate flask routes:
1. Help me write a flask app route to delete a garden from garden using a stored procedure.
2. I need help writing a delete route for the garden object (refactoring existing table and route code).
```

Line 233:
```
Date: 2/19/2026
Prompts used to generate flask routes:
1. Help me write a flask app route to delete a bed from bed using a stored procedure.
2. I need help writing a delete route for the bed object (refactoring existing table and route code).
```

Line 274:
```
Date: 2/19/2026
Prompts used to generate flask routes:
I need help refactoring the Insert route to utilize cursor.nextset() to consume result sets from MySQL stored procedures in Python.
AI Source URL: https://gemini.google.com/
```

Line 300:
```
Date: 3/4/2026
Prompts used for help with date input validation:
1. Help me refactor this function to vailidate date inputs
2. Gemini completely refactored the function but I only grabbed the necessary bits
```

Line 360:
```
Date: 3/4/2026
Prompts used for help with date input validation:
1. Help me refactor this function to vailidate date inputs
2. Gemini completely refactored the function but I only grabbed the necessary bits
```

### style.css
All work provided is original unless otherwise specified before
the code block.

#### Specific citations for style.css
Line 6:
```
No AI use, but google searched for font options:
Date: 03/04/2026
Searched google for font options and found Figtree and Vibur
```

Line 123:
```
Citation for use of AI Tools:
Date: 03/01/2026
Prompt used to generate CSS for a modern table. Create a modern form in the same style as the table
"Give me CSS for a modern table"
AI Source URL: https://claude.ai/
```

Line 340:
```
Date: 3/04/2026
Prompts used to refactor CSS:
1. Help me style an HTML anchor tag to look exactly like a button using my specific CSS properties.
2. Ensure the transition, padding, and hover colors remain consistent between the button and the link-based delete element.
AI Source URL: https://gemini.google.com/
```

### bed.j2
All code is based on the CS340 starter code or original unless otherwise noted.

#### Specific citations for bed.j2
Line 42:
```
Citation for use of AI Tools:
Date: 2/19/2026
Prompts used to generate on click confirmation for delete:
1. Help me write a on click confirmation for a delete button in html
AI Source URL: https://gemini.google.com/
```

### garden.j2
All code is based on the CS340 starter code or original unless otherwise noted.

#### Specific citations for garden.j2
Line 35:
```
Citation for use of AI Tools:
Date: 2/19/2026
Prompts used to generate on click confirmation for delete:
1. Help me write a on click confirmation for a delete button in html
AI Source URL: https://gemini.google.com/
```

### home.j2
All code is based on the CS340 starter code or original unless otherwise noted.

#### Specific citations for home.j2
Line 7:
```
Citation for use of AI Tools:
Date: 03/01/2026
Prompt used to generate website description
"Describe this website in a fun way for users using [website description]. Translate it to HTML"
AI Source URL: https://claude.ai/
```

### main.j2
All code is based on the CS340 starter code or original unless otherwise noted.

### plant_in_bed.j2
All code is based on the CS340 starter code or original unless otherwise noted.

#### Specific citations for plant_in_bed.j2
Line 5:
```
Citation for use of AI Tools:
Date: 3/4/2026
Prompts used for help with date input validation:
1. I pasted the HTML form code into the prompt and asked it to help me generate the
the renderings to show the error on the same page
```

Line 22:
```
Citation for use of AI Tools:
Date: 2/19/2026
Prompts used to refactor Jinja table:
I need help resolving the 'tuple object has no element 0' error.
AI Source URL: https://gemini.google.com/ 
```

Line 65:
```
Citation for use of AI Tools:
Date: 2/19/2026
Prompts used to refactor Jinja table and delete form:
1. I need help writing a delete route for the plant-in-bed object (formatting the HTML table and form).
2. Help me format the delete button inside the table.
AI Source URL: https://gemini.google.com/ 
```

Line 73:
```
Citation for use of AI Tools:
Date: 3/04/2026
Prompts used to refactor Jinja table and delete form:
1. Help me resolve an issue where the delete button requires multiple clicks to trigger.
2. Refactor the HTML form submission to use a styled link and dynamic JavaScript form creation to bypass browser event hijacking.
AI Source URL: https://gemini.google.com/
```

### plant.j2
All code is based on the CS340 starter code or original unless otherwise noted.

#### Specific citations for plant.j2
Line 48:
```
Citation for use of AI Tools:
Date: 2/19/2026
Prompts used to generate on click confirmation for delete:
1. Help me write a on click confirmation for a delete button in html
AI Source URL: https://gemini.google.com/
```

### update_plant_in_bed.j2
All code is based on the CS340 starter code or original unless otherwise noted.

#### Specific citations for update_plant_in_bed.j2
Line 5:
```
Citation for use of AI Tools:
Date: 3/4/2026
Prompts used for help with date input validation:
1. I pasted the HTML form code into the prompt and asked it to help me generate the
the renderings to show the error on the same page
```

### update_user.j2
All code is based on the CS340 starter code or original unless otherwise noted.

#### Specific citations for update_user.j2

### user.j2
All code is based on the CS340 starter code or original unless otherwise noted.

#### Specific citations for user.j2
Line 40:
```
Citation for use of AI Tools:
Date: 2/19/2026
Prompts used to generate on click confirmation for delete:
1. Help me write a on click confirmation for a delete button in html
AI Source URL: https://gemini.google.com/
```