# //// DESCRIZIONE \\\\\\\\

# //// STRUTTURA ALBERO \\\\\\\\

Overview della repository e delle varie sottocartelle:
- ****\<assets>****: dati e file in input utilizzati da tools e codice sorgente in modules
- **\<build>**: risultato di compilazione dei progetti di sviluppo in modules
  - **\<bin>**: contiene gli eseguibili
  - **\<libs>**: contiene le librerie
- **\<compilers>**: compilatori ed interpreti utilizzati per compilare codice ed eseguire script (e.g. 'mingw' o interprete Python)
- **\<docs>**: raccolta documenti utili allo sviluppo
- **\<modules>**: progetti di sviluppo suddivisi per componente e funzionalità
- **\<tools>**: script e progetti di supporto allo sviluppo dei progetti in modules (e.g. automazione task di varia natura)

# //// COMPILAZIONE ED ESECUZIONE \\\\\\\\

Guida alla compilazione ed esecuzione del codice sorgente e script di supporto. Il risultato dell'esecuzione dei file a seguire è determinato dal livello di profondità in cui si trova il file rispetto al root del repository:
- **\<build.bat>**: compila codice sorgente e sposta il risultato di compilazione in 'build' utilizzando i Makefile
- **\<run.bat>**: esegue risultato compilazione del codice sorgente
- **\<Makefile>**: file di configurazione per compilazione codice sorgente tramite utilizzo di 'mingw32-make.exe'

Questi file si basano sulla sulla presenza di compilatori ed interpreti opportuni, e sulla definizione delle seguenti variabili d'ambiente:
- **\<MAIN_DIR>**: percorso assoluto alla directory locale del repository
- **\<EXE_NAME>**: (opzionale) nome dell'eseguibile generato dal progetto di riferimento in fase di compilazione  
- **\<LIB_NAME>**: (opzionale) nome della libreria generata dal progetto di riferimento in fase di compilazione

# //// GIT \\\\\\\\
Guida all'uso di git per la condivisione della directory di lavoro.
- **\<branch>**:
  - **\<main>**: branch (origin) principale usato per avere l'ultima versione stabile del codice
  - **\<develop>**: branch (remote) di sviluppo usato per caricare le modifiche del codice
  - **\<personale>**: branch (remote) personale usato per le modifiche del codice 
- **\<comandi>**:
  - **\<git init>**: eseguito nel percorso della cartella esegue il setup iniziale della repository locale
  - **\<git clone [URL]>**: clona la repository remote (origin) in una repository locale
  - **\<git status>**: mostra lo stato dell'albero di lavoro
  - **\<git log>**: mostra le operazioni eseguite sulla repository (origin)
  - **\<git pull>**: incorpora i cambiamenti dalla remote repository nel branch corrente
  - **\<git add \*>**: aggiunge i cambiamenti e li prepara per la commit
  - **\<git commit -m [comment]>**: prepara i cambiamenti e li prepara per la push
  - **\<git push>**: push dei commit locali nella remote repository
  - **\<git branch [name]>**: creazione di un branch locale
  - **\<git branch -u [source] [name]>**: creazione di un remote branch
  - **\<git branch -d [name]>**: eliminazione di un branch locale
  - **\<git checkout [name]>**: switch del branch corrente
  - **\<git merge [source]>**: merge dei cambiamenti sul branch corrente da quello [source]

**Gestione branch personale**

Guida sul commit e push delle modifiche del branch personale sul branch develop
- **\<comandi>**:
  - **\<git add \*>**
  - **\<git commit -m [comment]>**
  - **\<git push>**
  - **\<git checkout develop>**
  - **\<git merge [branch personale]>**
  - **\<git push>**