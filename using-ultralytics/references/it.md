# Raw-Ultralytics - It

**Pages:** 39

---

## Addestramento del modello con Ultralytics YOLO

**URL:** https://docs.ultralytics.com/it/modes/train/

**Contents:**
- Addestramento del modello con Ultralytics YOLO
- Introduzione
- Perché scegliere Ultralytics YOLO per l'addestramento?
  - Caratteristiche principali della modalità Train
- Esempi di utilizzo
  - Training multi-GPU
  - Addestramento GPU inattiva
  - Addestramento MPS su Apple Silicon
  - Ripresa di addestramenti interrotti
- Impostazioni di Training

L'addestramento di un modello di deep learning implica l'alimentazione di dati e la regolazione dei suoi parametri affinché possa effettuare previsioni accurate. La modalità Train in Ultralytics YOLO26 è progettata per un addestramento efficace ed efficiente dei modelli di rilevamento oggetti, sfruttando appieno le moderne capacità hardware. Questa guida mira a coprire tutti i dettagli necessari per iniziare ad addestrare i propri modelli utilizzando il robusto set di funzionalità di YOLO26.

Guarda: Come addestrare un modello YOLO sul tuo set di dati personalizzato in Google Colab.

Ecco alcuni motivi convincenti per optare per la modalità Train di YOLO26:

Di seguito sono riportate alcune caratteristiche degne di nota della modalità Train di YOLO26:

Addestra YOLO26n sul dataset COCO8 per 100 epoche con una dimensione dell'immagine di 640. Il dispositivo di training può essere specificato utilizzando l'argomento device argomento. Se non viene passato alcun argomento, la GPU device=0 verrà utilizzata quando disponibile; altrimenti la device='cpu' verrà utilizzata. Per un elenco completo degli argomenti di training, consultare la sezione Argomenti di seguito.

Errore di Multi-Processing di Windows

Su Windows, potresti ricevere un RuntimeError quando si avvia l'addestramento come script. Aggiungere un if __name__ == "__main__": aggiungi questo blocco prima del tuo codice di training per risolverlo.

Esempio di training su singola GPU e CPU

Il dispositivo viene determinato automaticamente. Se è disponibile una GPU, verrà utilizzata (dispositivo CUDA predefinito 0); altrimenti il training inizierà sulla CPU.

Il training multi-GPU consente un utilizzo più efficiente delle risorse hardware disponibili distribuendo il carico di training su più GPU. Questa funzionalità è disponibile sia tramite l'API python che tramite l'interfaccia a riga di comando. Per abilitare il training multi-GPU, specifica gli ID dei dispositivi GPU che desideri utilizzare.

Esempio di training multi-GPU

Per eseguire il training con 2 GPU, dispositivi CUDA 0 e 1, utilizza i seguenti comandi. Espandi a GPU aggiuntive secondo necessità.

L'addestramento GPU inattiva consente la selezione automatica delle GPU meno utilizzate nei sistemi multi-GPU, ottimizzando l'utilizzo delle risorse senza selezione manuale della GPU. Questa funzionalità identifica le GPU disponibili in base alle metriche di utilizzo e alla disponibilità di VRAM.

Esempio di addestramento GPU inattiva

Per selezionare e utilizzare automaticamente le GPU più inattive per il training, usa il -1 parametro device. Ciò è particolarmente utile in ambienti di calcolo condivisi o server con più utenti.

L'algoritmo di selezione automatica dà la priorità alle GPU con:

Questa funzionalità è particolarmente utile in ambienti di calcolo condivisi o quando si eseguono più processi di addestramento su modelli diversi. Si adatta automaticamente alle mutevoli condizioni del sistema, garantendo un'allocazione ottimale delle risorse senza intervento manuale.

Grazie al supporto per i chip Apple Silicon integrati nei modelli Ultralytics YOLO, ora è possibile eseguire il training dei modelli su dispositivi che utilizzano il potente framework Metal Performance Shaders (MPS). MPS offre un modo ad alte prestazioni per eseguire attività di calcolo ed elaborazione delle immagini sul silicio personalizzato di Apple.

Per abilitare il training sui chip Apple Silicon, è necessario specificare 'mps' come dispositivo quando si avvia il processo di training. Di seguito è riportato un esempio di come è possibile farlo in python e tramite la riga di comando:

Esempio di training MPS

Sfruttando la potenza di calcolo dei chip Apple Silicon, ciò consente un'elaborazione più efficiente delle attività di training. Per una guida più dettagliata e opzioni di configurazione avanzate, fare riferimento alla documentazione PyTorch MPS.

La ripresa del training da uno stato precedentemente salvato è una funzionalità cruciale quando si lavora con modelli di deep learning. Questo può essere utile in vari scenari, come quando il processo di training è stato interrotto inaspettatamente o quando si desidera continuare a eseguire il training di un modello con nuovi dati o per più epoche.

Quando il training viene ripreso, Ultralytics YOLO carica i pesi dall'ultimo modello salvato e ripristina anche lo stato dell'ottimizzatore, lo scheduler del learning rate e il numero di epoca. Ciò consente di continuare il processo di training senza interruzioni da dove era stato interrotto.

È possibile riprendere facilmente l'addestramento in Ultralytics YOLO impostando l'argomento resume a True quando si richiama il metodo train e specificando il percorso del file .pt contenente i pesi del modello parzialmente addestrato.

Di seguito è riportato un esempio di come riprendere un addestramento interrotto utilizzando python e tramite la riga di comando:

Esempio di ripresa dell'addestramento

Impostando resume=True, la funzione train continuerà l'addestramento da dove era stato interrotto, utilizzando lo stato memorizzato nel file 'path\/to\/last.pt'. Se l'argomento resume viene omesso o impostato su False, la funzione train , la funzione avvierà una nuova sessione di addestramento.

Ricorda che i checkpoint vengono salvati alla fine di ogni epoca per impostazione predefinita, o a intervalli fissi utilizzando l'argomento save_period , quindi è necessario completare almeno 1 epoca per riprendere un'esecuzione di addestramento.

Le impostazioni di addestramento per i modelli YOLO comprendono vari iperparametri e configurazioni utilizzati durante il processo di addestramento. Queste impostazioni influenzano le prestazioni, la velocità e l'accuratezza del modello. Le impostazioni chiave dell'addestramento includono la dimensione del batch, il tasso di apprendimento, il momentum e il decadimento del peso. Inoltre, la scelta dell'ottimizzatore, della funzione di perdita e della composizione del set di dati di addestramento può influire sul processo di addestramento. Un'attenta messa a punto e la sperimentazione con queste impostazioni sono fondamentali per ottimizzare le prestazioni.

Nota sulle impostazioni della dimensione del batch

Il batch L'argomento può essere configurato in tre modi:

Le tecniche di augmentation sono essenziali per migliorare la robustezza e le prestazioni dei modelli YOLO introducendo variabilità nei dati di addestramento, aiutando il modello a generalizzare meglio a dati non ancora visti. La tabella seguente descrive lo scopo e l'effetto di ciascun argomento di augmentation:

Queste impostazioni possono essere regolate per soddisfare i requisiti specifici del set di dati e dell'attività da svolgere. Sperimentare con valori diversi può aiutare a trovare la strategia di augmentation ottimale che porta alle migliori prestazioni del modello.

Per ulteriori informazioni sulle operazioni di aumento dell'addestramento, consultare la sezione di riferimento.

Nell'addestramento di un modello YOLO26, potrebbe essere utile tenere traccia delle prestazioni del modello nel tempo. È qui che entra in gioco il logging. Ultralytics YOLO fornisce supporto per tre tipi di logger: Comet, ClearML e TensorBoard.

Per utilizzare un logger, selezionalo dal menu a tendina nello snippet di codice qui sopra ed eseguilo. Il logger scelto verrà installato e inizializzato.

Comet è una piattaforma che consente a data scientist e sviluppatori di monitorare, confrontare, spiegare e ottimizzare esperimenti e modelli. Fornisce funzionalità come metriche in tempo reale, differenze di codice e monitoraggio degli iperparametri.

Per utilizzare Comet:

Ricordati di accedere al tuo account Comet sul loro sito web e di ottenere la tua chiave API. Dovrai aggiungerla alle tue variabili d'ambiente o al tuo script per registrare i tuoi esperimenti.

ClearML è una piattaforma open-source che automatizza il tracciamento degli esperimenti e aiuta a condividere le risorse in modo efficiente. È progettata per aiutare i team a gestire, eseguire e riprodurre il proprio lavoro di ML in modo più efficiente.

Per utilizzare ClearML:

Dopo aver eseguito questo script, dovrai accedere al tuo account ClearML sul browser e autenticare la tua sessione.

TensorBoard è un toolkit di visualizzazione per TensorFlow. Ti permette di visualizzare il tuo grafo TensorFlow, tracciare metriche quantitative sull'esecuzione del tuo grafo e mostrare dati aggiuntivi come le immagini che lo attraversano.

Per utilizzare TensorBoard in Google Colab:

Per utilizzare TensorBoard localmente, esegui il comando seguente e visualizza i risultati su http://localhost:6006/.

Questo caricherà TensorBoard e lo indirizzerà alla directory in cui sono salvati i log di training.

Dopo aver configurato il logger, puoi procedere con il training del modello. Tutte le metriche di training verranno automaticamente registrate nella piattaforma scelta e potrai accedere a questi log per monitorare le prestazioni del tuo modello nel tempo, confrontare diversi modelli e identificare aree di miglioramento.

Per addestrare un modello di rilevamento oggetti utilizzando Ultralytics YOLO26, è possibile utilizzare l'API Python o la CLI. Di seguito è riportato un esempio per entrambi:

Esempio di training su singola GPU e CPU

Per maggiori dettagli, consulta la sezione Impostazioni di addestramento.

Le caratteristiche principali della modalità Train di Ultralytics YOLO26 includono:

Queste funzionalità rendono l'addestramento efficiente e personalizzabile in base alle tue esigenze. Per maggiori dettagli, consulta la sezione Funzionalità chiave della modalità Train.

Per riprendere l'addestramento da una sessione interrotta, imposta il parametro resume a True e specifica il percorso dell'ultimo checkpoint salvato.

Esempio di ripresa dell'addestramento

Consulta la sezione su Ripresa di addestramenti interrotti per maggiori informazioni.

Sì, Ultralytics YOLO26 supporta l'addestramento su chip Apple silicon utilizzando il framework Metal Performance Shaders (MPS). Specificare 'mps' come dispositivo di addestramento.

Esempio di training MPS

Per maggiori dettagli, consulta la sezione Addestramento MPS su Apple Silicon.

Ultralytics YOLO26 consente di configurare una varietà di impostazioni di addestramento, come la dimensione del batch, il tasso di apprendimento, le epoche e altro ancora, tramite argomenti. Ecco una breve panoramica:

Per una guida approfondita sulle impostazioni di training, consulta la sezione Impostazioni di training.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.yaml")  # build a new model from YAML
model = YOLO("yolo26n.pt")  # load a pretrained model (recommended for training)
model = YOLO("yolo26n.yaml").load("yolo26n.pt")  # build from YAML and transfer weights

# Train the model
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

Example 2 (sql):
```sql
# Build a new model from YAML and start training from scratch
yolo detect train data=coco8.yaml model=yolo26n.yaml epochs=100 imgsz=640

# Start training from a pretrained *.pt model
yolo detect train data=coco8.yaml model=yolo26n.pt epochs=100 imgsz=640

# Build a new model from YAML, transfer pretrained weights to it and start training
yolo detect train data=coco8.yaml model=yolo26n.yaml pretrained=yolo26n.pt epochs=100 imgsz=640
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load a pretrained model (recommended for training)

# Train the model with 2 GPUs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640, device=[0, 1])

# Train the model with the two most idle GPUs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640, device=[-1, -1])
```

Example 4 (julia):
```julia
# Start training from a pretrained *.pt model using GPUs 0 and 1
yolo detect train data=coco8.yaml model=yolo26n.pt epochs=100 imgsz=640 device=0,1

# Use the two most idle GPUs
yolo detect train data=coco8.yaml model=yolo26n.pt epochs=100 imgsz=640 device=-1,-1
```

---

## Aiuto

**URL:** https://docs.ultralytics.com/it/help/

**Contents:**
- Aiuto
- FAQ
  - Cos'è Ultralytics YOLO e come può essere utile per i miei progetti di machine learning?
  - Come posso contribuire ai repository Ultralytics YOLO?
  - Perché dovrei utilizzare la piattaforma Ultralytics per i miei progetti di machine learning?
  - Cos'è l'integrazione continua (CI) in Ultralytics e come garantisce un codice di alta qualità?
  - Come viene gestita la privacy dei dati da Ultralytics?
- Commenti

Benvenuti alla pagina di aiuto di Ultralytics. Questa pagina raccoglie guide pratiche, politiche e FAQ per supportare il vostro lavoro con i modelli e i repository Ultralytics YOLO.

Vi incoraggiamo a consultare queste risorse per un'esperienza fluida e produttiva. Se avete bisogno di ulteriore supporto, contattateci tramite GitHub Issues o la Community Ultralytics.

Ultralytics YOLO (You Only Look Once) è un modello all'avanguardia per il rilevamento di oggetti in tempo reale. La sua ultima versione, YOLO26, offre un'inferenza più veloce, leggera e end-to-end, priva di NMS, ottimizzata per dispositivi edge e a basso consumo, rendendola ideale per un'ampia gamma di applicazioni, dall'analisi video in tempo reale alla ricerca avanzata nel machine learning. L'efficienza di YOLO nel detect oggetti in immagini e video l'ha resa la soluzione di riferimento per aziende e ricercatori che desiderano integrare robuste capacità di visione artificiale nei loro progetti.

Per maggiori dettagli su YOLO26, visita la documentazione di YOLO26.

Contribuire ai repository Ultralytics YOLO è semplice. Inizia consultando la Guida per i contributi per comprendere i protocolli per l'invio di pull request, la segnalazione di bug e altro ancora. Dovrai anche firmare il Contratto di licenza per i collaboratori (CLA) per garantire che i tuoi contributi siano legalmente riconosciuti. Per una segnalazione efficace dei bug, fai riferimento alla Guida all'esempio minimo riproducibile (MRE).

Ultralytics Platform offre una soluzione no-code e senza interruzioni per la gestione dei tuoi progetti di machine learning. Ti consente di generare, addestrare e deploy modelli AI come YOLO26 senza sforzo. Le funzionalità uniche includono l'addestramento in cloud, il track in tempo reale e la gestione intuitiva dei dataset. Ultralytics Platform semplifica l'intero flusso di lavoro, dall'elaborazione dei dati al deployment del modello, rendendolo uno strumento indispensabile sia per i principianti che per gli utenti esperti.

Per iniziare, visita la Guida Rapida di Ultralytics Platform.

L'integrazione continua (CI) in Ultralytics prevede processi automatizzati che garantiscono l'integrità e la qualità del codebase. La nostra configurazione CI include il deployment Docker, i controlli dei link non funzionanti, l'analisi CodeQL e la pubblicazione su PyPI. Questi processi aiutano a mantenere repository stabili e sicuri eseguendo automaticamente test e controlli sui nuovi invii di codice.

Per saperne di più, consulta la Guida all'integrazione continua (CI).

Ultralytics prende molto sul serio la privacy dei dati. La nostra Informativa sulla privacy descrive come raccogliamo e utilizziamo i dati anonimizzati per migliorare il pacchetto YOLO, dando al contempo priorità alla privacy e al controllo dell'utente. Aderiamo a rigide normative sulla protezione dei dati per garantire che le tue informazioni siano sempre al sicuro.

Per maggiori informazioni, consulta la nostra Informativa sulla privacy.

---

## Benchmark del modello con Ultralytics YOLO

**URL:** https://docs.ultralytics.com/it/modes/benchmark/

**Contents:**
- Benchmark del modello con Ultralytics YOLO
- Visualizzazione del benchmark
- Introduzione
- Perché il benchmarking è fondamentale?
  - Metriche chiave nella modalità benchmark
  - Formati di esportazione supportati
- Esempi di utilizzo
- Argomenti
- Formati di esportazione
- FAQ

Potrebbe essere necessario aggiornare la pagina per visualizzare correttamente i grafici a causa di potenziali problemi con i cookie.

Una volta che il modello è stato addestrato e validato, il passo logico successivo è valutarne le prestazioni in vari scenari del mondo reale. La modalità Benchmark in Ultralytics YOLO26 serve a questo scopo fornendo un framework robusto per valutare la velocità e l'accuratezza del modello su una gamma di formati di esportazione.

Guarda: Benchmark dei modelli Ultralytics YOLO26 | Come confrontare le prestazioni dei modelli su hardware diversi?

Esegui i benchmark di YOLO26n su tutti i formati di esportazione supportati (ONNX, TensorRT, ecc.). Consulta la sezione Argomenti di seguito per un elenco completo delle opzioni di esportazione.

Argomenti come model, data, imgsz, half, device, verbose e format offrono agli utenti la flessibilità di mettere a punto i benchmark in base alle loro esigenze specifiche e di confrontare facilmente le prestazioni di diversi formati di esportazione.

I benchmark tenteranno di essere eseguiti automaticamente su tutti i formati di esportazione possibili elencati di seguito. In alternativa, puoi eseguire benchmark per un formato specifico utilizzando il format argomento, che accetta uno qualsiasi dei formati menzionati di seguito.

Vedi tutti i export dettagli nella Esportazione pagina.

Ultralytics YOLO26 offre una modalità Benchmark per valutare le prestazioni del tuo modello su diversi formati di esportazione. Questa modalità fornisce approfondimenti su metriche chiave come la precisione media (mAP50-95), l'accuratezza e il tempo di inferenza in millisecondi. Per eseguire i benchmark, puoi utilizzare comandi Python o CLI. Ad esempio, per eseguire il benchmark su una GPU:

Per maggiori dettagli sugli argomenti del benchmark, visita la sezione Argomenti.

Esportare i modelli YOLO26 in diversi formati come ONNX, TensorRT e OpenVINO consente di ottimizzare le prestazioni in base all'ambiente di deployment. Ad esempio:

Questi formati migliorano sia la velocità che l'accuratezza dei tuoi modelli, rendendoli più efficienti per varie applicazioni nel mondo reale. Visita la pagina Esportazione per tutti i dettagli.

Il benchmarking dei tuoi modelli YOLO26 è essenziale per diverse ragioni:

Metriche chiave come mAP50-95, accuratezza Top-5 e tempo di inferenza aiutano nel fare queste valutazioni. Fare riferimento alla sezione Metriche Chiave per maggiori informazioni.

YOLO26 supporta una varietà di formati di esportazione, ciascuno ottimizzato per hardware e casi d'uso specifici:

Per un elenco completo dei formati supportati e dei rispettivi vantaggi, consulta la sezione Formati di esportazione supportati.

Durante l'esecuzione dei benchmark, è possibile personalizzare diversi argomenti per soddisfare esigenze specifiche:

Per un elenco completo degli argomenti, consultare la sezione Argomenti.

**Examples:**

Example 1 (sql):
```sql
from ultralytics.utils.benchmarks import benchmark

# Benchmark on GPU
benchmark(model="yolo26n.pt", data="coco8.yaml", imgsz=640, half=False, device=0)

# Benchmark specific export format
benchmark(model="yolo26n.pt", data="coco8.yaml", imgsz=640, format="onnx")
```

Example 2 (markdown):
```markdown
yolo benchmark model=yolo26n.pt data='coco8.yaml' imgsz=640 half=False device=0

# Benchmark specific export format
yolo benchmark model=yolo26n.pt data='coco8.yaml' imgsz=640 format=onnx
```

Example 3 (sql):
```sql
from ultralytics.utils.benchmarks import benchmark

# Benchmark on GPU
benchmark(model="yolo26n.pt", data="coco8.yaml", imgsz=640, half=False, device=0)
```

Example 4 (unknown):
```unknown
yolo benchmark model=yolo26n.pt data='coco8.yaml' imgsz=640 half=False device=0
```

---

## Classificazione delle immagini

**URL:** https://docs.ultralytics.com/it/tasks/classify/

**Contents:**
- Classificazione delle immagini
- Modelli
- Addestramento
  - Formato del set di dati
- Valutazione
- Predizione
- Esportazione
- FAQ
  - Qual è lo scopo di YOLO26 nella classificazione delle immagini?
  - Come si addestra un modello YOLO26 per la classificazione delle immagini?

La classificazione delle immagini è la più semplice delle tre attività e comporta la classificazione di un'intera immagine in una di una serie di classi predefinite.

L'output di un classificatore di immagini è una singola etichetta di classe e un punteggio di confidenza. La classificazione delle immagini è utile quando è necessario sapere solo a quale classe appartiene un'immagine e non è necessario sapere dove si trovano gli oggetti di quella classe o qual è la loro forma esatta.

Guarda: Esplora le Funzionalità YOLO di Ultralytics: Classificazione di Immagini utilizzando la Piattaforma Ultralytics

I modelli YOLO26 Classify utilizzano il -cls suffisso, ad esempio, yolo26n-cls.pt, e sono pre-addestrati su ImageNet.

I modelli YOLO26 Classify pre-addestrati sono mostrati qui. I modelli Detect, Segment e Pose sono pre-addestrati sul dataset COCO, mentre i modelli Classify sono pre-addestrati sul dataset ImageNet.

I modelli vengono scaricati automaticamente dall'ultima release di Ultralytics al primo utilizzo.

Addestra YOLO26n-cls sul dataset MNIST160 per 100 epoche alla dimensione dell'immagine di 64. Per un elenco completo degli argomenti disponibili, consulta la pagina Configurazione.

La classificazione Ultralytics YOLO utilizza torchvision.transforms.RandomResizedCrop per l'addestramento e torchvision.transforms.CenterCrop per la validazione e l'inferenza. Queste trasformazioni basate sul ritaglio presuppongono input quadrati e possono inavvertitamente ritagliare regioni importanti da immagini con proporzioni estreme, causando potenzialmente la perdita di informazioni visive critiche durante l'addestramento. Per preservare l'immagine completa mantenendone le proporzioni, considera l'utilizzo di torchvision.transforms.Resize invece delle trasformazioni di ritaglio.

Puoi implementare questo personalizzando la tua pipeline di aumento tramite un ClassificationDataset e ClassificationTrainer.

Il formato del dataset di classificazione YOLO può essere trovato in dettaglio nella Guida al dataset.

Valida il modello YOLO26n-cls addestrato accuratezza sul dataset MNIST160. Non sono necessari argomenti poiché il model mantiene il suo training data e gli argomenti come attributi del modello.

Come menzionato in sezione di training, puoi gestire proporzioni estreme durante l'addestramento utilizzando un ClassificationTrainer. È necessario applicare lo stesso approccio per ottenere risultati di convalida coerenti implementando un ClassificationValidator quando si richiama il metodo val() metodo. Fare riferimento all'esempio di codice completo nella sezione di training per i dettagli di implementazione.

Utilizza un modello YOLO26n-cls addestrato per eseguire previsioni sulle immagini.

Vedi tutti i predict dettagli della modalità nella Predizione pagina.

Esporta un modello YOLO26n-cls in un formato diverso come ONNX, CoreML, ecc.

I formati di esportazione YOLO26-cls disponibili sono nella tabella seguente. Puoi esportare in qualsiasi formato utilizzando il format argomento, cioè, format='onnx' oppure format='engine'. È possibile effettuare previsioni o validazioni direttamente sui modelli esportati, cioè, yolo predict model=yolo26n-cls.onnx. Esempi di utilizzo vengono mostrati per il tuo modello dopo che l'esportazione è stata completata.

Vedi tutti i export dettagli nella Esportazione pagina.

I modelli YOLO26, come yolo26n-cls.pt, sono progettati per una classificazione efficiente delle immagini. Assegnano una singola etichetta di classe a un'intera immagine insieme a un punteggio di confidenza. Ciò è particolarmente utile per le applicazioni in cui è sufficiente conoscere la classe specifica di un'immagine, piuttosto che identificare la posizione o la forma degli oggetti all'interno dell'immagine.

Per addestrare un modello YOLO26, puoi utilizzare comandi Python o CLI. Ad esempio, per addestrare un yolo26n-cls modello sul dataset MNIST160 per 100 epoche con una dimensione dell'immagine di 64:

Per ulteriori opzioni di configurazione, visita la pagina Configurazione.

I modelli di classificazione YOLO26 pre-addestrati possono essere trovati nel Modelli sezione. Modelli come yolo26n-cls.pt, yolo26s-cls.pt, yolo26m-cls.pt, ecc., sono pre-addestrati sul ImageNet dataset e possono essere facilmente scaricati e utilizzati per varie attività di classificazione delle immagini.

Puoi esportare un modello YOLO26 addestrato in vari formati utilizzando comandi Python o CLI. Ad esempio, per esportare un modello in formato ONNX:

Per opzioni di esportazione dettagliate, consulta la pagina Esportazione.

Per convalidare l'accuratezza di un modello addestrato su un dataset come MNIST160, puoi utilizzare i seguenti comandi Python o CLI:

Per ulteriori informazioni, visita la sezione Convalida.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-cls.yaml")  # build a new model from YAML
model = YOLO("yolo26n-cls.pt")  # load a pretrained model (recommended for training)
model = YOLO("yolo26n-cls.yaml").load("yolo26n-cls.pt")  # build from YAML and transfer weights

# Train the model
results = model.train(data="mnist160", epochs=100, imgsz=64)
```

Example 2 (sql):
```sql
# Build a new model from YAML and start training from scratch
yolo classify train data=mnist160 model=yolo26n-cls.yaml epochs=100 imgsz=64

# Start training from a pretrained *.pt model
yolo classify train data=mnist160 model=yolo26n-cls.pt epochs=100 imgsz=64

# Build a new model from YAML, transfer pretrained weights to it and start training
yolo classify train data=mnist160 model=yolo26n-cls.yaml pretrained=yolo26n-cls.pt epochs=100 imgsz=64
```

Example 3 (python):
```python
import torch
import torchvision.transforms as T

from ultralytics import YOLO
from ultralytics.data.dataset import ClassificationDataset
from ultralytics.models.yolo.classify import ClassificationTrainer, ClassificationValidator


class CustomizedDataset(ClassificationDataset):
    """A customized dataset class for image classification with enhanced data augmentation transforms."""

    def __init__(self, root: str, args, augment: bool = False, prefix: str = ""):
        """Initialize a customized classification dataset with enhanced data augmentation transforms."""
        super().__init__(root, args, augment, prefix)

        # Add your custom training transforms here
        train_transforms = T.Compose(
            [
                T.Resize((args.imgsz, args.imgsz)),
                T.RandomHorizontalFlip(p=args.fliplr),
                T.RandomVerticalFlip(p=args.flipud),
                T.RandAugment(interpolation=T.InterpolationMode.BILINEAR),
                T.ColorJitter(brightness=args.hsv_v, contrast=args.hsv_v, saturation=args.hsv_s, hue=args.hsv_h),
                T.ToTensor(),
                T.Normalize(mean=torch.tensor(0), std=torch.tensor(1)),
                T.RandomErasing(p=args.erasing, inplace=True),
            ]
        )

        # Add your custom validation transforms here
        val_transforms = T.Compose(
            [
                T.Resize((args.imgsz, args.imgsz)),
                T.ToTensor(),
                T.Normalize(mean=torch.tensor(0), std=torch.tensor(1)),
            ]
        )
        self.torch_transforms = train_transforms if augment else val_transforms


class CustomizedTrainer(ClassificationTrainer):
    """A customized trainer class for YOLO classification models with enhanced dataset handling."""

    def build_dataset(self, img_path: str, mode: str = "train", batch=None):
        """Build a customized dataset for classification training and the validation during training."""
        return CustomizedDataset(root=img_path, args=self.args, augment=mode == "train", prefix=mode)


class CustomizedValidator(ClassificationValidator):
    """A customized validator class for YOLO classification models with enhanced dataset handling."""

    def build_dataset(self, img_path: str, mode: str = "train"):
        """Build a customized dataset for classification standalone validation."""
        return CustomizedDataset(root=img_path, args=self.args, augment=mode == "train", prefix=self.args.split)


model = YOLO("yolo26n-cls.pt")
model.train(data="imagenet1000", trainer=CustomizedTrainer, epochs=10, imgsz=224, batch=64)
model.val(data="imagenet1000", validator=CustomizedValidator, imgsz=224, batch=64)
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-cls.pt")  # load an official model
model = YOLO("path/to/best.pt")  # load a custom model

# Validate the model
metrics = model.val()  # no arguments needed, dataset and settings remembered
metrics.top1  # top1 accuracy
metrics.top5  # top5 accuracy
```

---

## Efficient Hyperparameter Tuning with Ray Tune and YOLO26

**URL:** https://docs.ultralytics.com/integrations/ray-tune/

**Contents:**
- Efficient Hyperparameter Tuning with Ray Tune and YOLO26
- Accelerate Tuning with Ultralytics YOLO26 and Ray Tune
  - Ray Tune
  - Integration with Weights & Biases
- Installation
- Usage
- tune() Method Parameters
- Default Search Space Description
- Custom Search Space Example
- Resuming An Interrupted Hyperparameter Tuning Session With Ray Tune

Hyperparameter tuning is vital in achieving peak model performance by discovering the optimal set of hyperparameters. This involves running trials with different hyperparameters and evaluating each trial's performance.

Ultralytics YOLO26 incorporates Ray Tune for hyperparameter tuning, streamlining the optimization of YOLO26 model hyperparameters. With Ray Tune, you can utilize advanced search strategies, parallelism, and early stopping to expedite the tuning process.

Ray Tune is a hyperparameter tuning library designed for efficiency and flexibility. It supports various search strategies, parallelism, and early stopping strategies, and seamlessly integrates with popular machine learning frameworks, including Ultralytics YOLO26.

YOLO26 also allows optional integration with Weights & Biases for monitoring the tuning process.

To install the required packages, run:

The tune() method in YOLO26 provides an easy-to-use interface for hyperparameter tuning with Ray Tune. It accepts several arguments that allow you to customize the tuning process. Below is a detailed explanation of each parameter:

By customizing these parameters, you can fine-tune the hyperparameter optimization process to suit your specific needs and available computational resources.

The following table lists the default search space parameters for hyperparameter tuning in YOLO26 with Ray Tune. Each parameter has a specific value range defined by tune.uniform().

In this example, we demonstrate how to use a custom search space for hyperparameter tuning with Ray Tune and YOLO26. By providing a custom search space, you can focus the tuning process on specific hyperparameters of interest.

In the code snippet above, we create a YOLO model with the "yolo26n.pt" pretrained weights. Then, we call the tune() method, specifying the dataset configuration with "coco8.yaml". We provide a custom search space for the initial learning rate lr0 using a dictionary with the key "lr0" and the value tune.uniform(1e-5, 1e-1). Finally, we pass additional training arguments, such as the number of epochs directly to the tune method as epochs=50.

You can resume an interrupted Ray Tune session by passing resume=True. You can optionally pass the directory name used by Ray Tune under runs/{task} to resume. Otherwise, it would resume the last interrupted session. You don't need to provide the iterations and space again, but you need to provide the rest of the training arguments again including data and epochs.

Using resume=True with model.tune()

After running a hyperparameter tuning experiment with Ray Tune, you might want to perform various analyses on the obtained results. This guide will take you through common workflows for processing and analyzing these results.

After running the tuning experiment with tuner.fit(), you can load the results from a directory. This is useful, especially if you're performing the analysis after the initial training script has exited.

Get an overview of how trials performed. You can quickly check if there were any errors during the trials.

Access individual trial hyperparameter configurations and the last reported metrics.

You can plot the history of reported metrics for each trial to see how the metrics evolved over time.

In this guide, we covered common workflows to analyze the results of experiments run with Ray Tune using Ultralytics. The key steps include loading the experiment results from a directory, performing basic experiment-level and trial-level analysis, and plotting metrics.

Explore further by looking into Ray Tune's Analyze Results docs page to get the most out of your hyperparameter tuning experiments.

To tune the hyperparameters of your Ultralytics YOLO26 model using Ray Tune, follow these steps:

Install the required packages:

Load your YOLO26 model and start tuning:

This utilizes Ray Tune's advanced search strategies and parallelism to efficiently optimize your model's hyperparameters. For more information, check out the Ray Tune documentation.

Ultralytics YOLO26 uses the following default hyperparameters for tuning with Ray Tune:

These hyperparameters can be customized to suit your specific needs. For a complete list and more details, refer to the Hyperparameter Tuning guide.

To integrate Weights & Biases (W&B) with your Ultralytics YOLO26 tuning process:

Modify your tuning script:

This setup will allow you to monitor the tuning process, track hyperparameter configurations, and visualize results in W&B.

Ray Tune offers numerous advantages for hyperparameter optimization:

Ray Tune seamlessly integrates with Ultralytics YOLO26, providing an easy-to-use interface for tuning hyperparameters effectively. To get started, check out the Hyperparameter Tuning guide.

To define a custom search space for your YOLO26 hyperparameter tuning with Ray Tune:

This customizes the range of hyperparameters like initial learning rate and momentum to be explored during the tuning process. For advanced configurations, refer to the Custom Search Space Example section.

**Examples:**

Example 1 (sql):
```sql
# Install and update Ultralytics and Ray Tune packages
pip install -U ultralytics "ray[tune]"

# Optionally install W&B for logging
pip install wandb
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a YOLO26n model
model = YOLO("yolo26n.pt")

# Start tuning hyperparameters for YOLO26n training on the COCO8 dataset
result_grid = model.tune(data="coco8.yaml", use_ray=True)
```

Example 3 (python):
```python
from ray import tune

from ultralytics import YOLO

# Define a YOLO model
model = YOLO("yolo26n.pt")

# Run Ray Tune on the model
result_grid = model.tune(
    data="coco8.yaml",
    space={"lr0": tune.uniform(1e-5, 1e-1)},
    epochs=50,
    use_ray=True,
)
```

Example 4 (python):
```python
from ultralytics import YOLO

# Define a YOLO model
model = YOLO("yolo26n.pt")

# Resume previous run
results = model.tune(use_ray=True, data="coco8.yaml", epochs=50, resume=True)

# Resume Ray Tune run with name 'tune_exp_2'
results = model.tune(use_ray=True, data="coco8.yaml", epochs=50, name="tune_exp_2", resume=True)
```

---

## Esportazione di modelli con Ultralytics YOLO

**URL:** https://docs.ultralytics.com/it/modes/export/

**Contents:**
- Esportazione di modelli con Ultralytics YOLO
- Introduzione
- Perché scegliere la modalità di esportazione di YOLO26?
  - Caratteristiche principali della modalità di esportazione
- Esempi di utilizzo
- Argomenti
- Formati di esportazione
- FAQ
  - Come si esporta un modello YOLO26 nel formato ONNX?
  - Quali sono i vantaggi dell'utilizzo di TensorRT per l'esportazione del modello?

L'obiettivo finale dell'addestramento di un modello è distribuirlo per applicazioni nel mondo reale. La modalità di esportazione in Ultralytics YOLO26 offre una gamma versatile di opzioni per esportare il modello addestrato in diversi formati, rendendolo distribuibile su varie piattaforme e dispositivi. Questa guida completa mira a illustrare le sfumature dell'esportazione del modello, mostrando come ottenere la massima compatibilità e prestazioni.

Guarda: Come esportare un modello Ultralytics YOLO addestrato personalizzato ed eseguire l'inferenza in tempo reale su webcam.

Ecco alcune delle funzionalità più importanti:

Esporta un modello YOLO26n in un formato diverso come ONNX o TensorRT. Consulta la sezione Argomenti di seguito per un elenco completo degli argomenti di esportazione.

Questa tabella descrive in dettaglio le configurazioni e le opzioni disponibili per l'esportazione di modelli YOLO in diversi formati. Queste impostazioni sono fondamentali per ottimizzare le prestazioni, le dimensioni e la compatibilità del modello esportato su varie piattaforme e ambienti. Una configurazione corretta garantisce che il modello sia pronto per l'implementazione nell'applicazione prevista con la massima efficienza.

La regolazione di questi parametri consente la personalizzazione del processo di esportazione per adattarsi a requisiti specifici, come l'ambiente di implementazione, i vincoli hardware e gli obiettivi di prestazioni. La selezione del formato e delle impostazioni appropriati è essenziale per ottenere il miglior equilibrio tra dimensioni del modello, velocità e precisione.

I formati di esportazione YOLO26 disponibili sono nella tabella sottostante. Puoi esportare in qualsiasi formato usando il format argomento, cioè, format='onnx' oppure format='engine'. È possibile effettuare previsioni o validazioni direttamente sui modelli esportati, cioè, yolo predict model=yolo26n.onnx. Esempi di utilizzo vengono mostrati per il tuo modello dopo che l'esportazione è stata completata.

Esportare un modello YOLO26 in formato ONNX è semplice con Ultralytics. Fornisce metodi sia Python che CLI per l'esportazione dei modelli.

Per maggiori dettagli sul processo, comprese le opzioni avanzate come la gestione di diverse dimensioni di input, fare riferimento alla guida all'integrazione ONNX.

L'utilizzo di TensorRT per l'esportazione dei modelli offre miglioramenti significativi delle prestazioni. I modelli YOLO26 esportati in TensorRT possono raggiungere un'accelerazione della GPU fino a 5 volte, rendendoli ideali per applicazioni di inferenza in tempo reale.

Per saperne di più sull'integrazione di TensorRT, consulta la guida all'integrazione di TensorRT.

La quantizzazione INT8 è un ottimo modo per comprimere il modello e accelerare l'inferenza, specialmente sui dispositivi edge. Ecco come puoi abilitare la quantizzazione INT8:

La quantizzazione INT8 può essere applicata a vari formati, come TensorRT, OpenVINO, e CoreML. Per risultati di quantizzazione ottimali, fornire un elemento rappresentativo dataset utilizzando il data parametro.

La dimensione di input dinamica consente al modello esportato di gestire dimensioni dell'immagine variabili, offrendo flessibilità e ottimizzando l'efficienza di elaborazione per diversi casi d'uso. Quando si esporta in formati come ONNX o TensorRT, abilitare la dimensione di input dinamica assicura che il modello possa adattarsi senza problemi a diverse forme di input.

Per abilitare questa funzionalità, usa il flag dynamic=True durante l'esportazione:

Il dimensionamento dinamico dell'input è particolarmente utile per applicazioni in cui le dimensioni dell'input possono variare, come l'elaborazione video o la gestione di immagini provenienti da fonti diverse.

Comprendere e configurare gli argomenti di esportazione è fondamentale per ottimizzare le prestazioni del modello:

Per la distribuzione su piattaforme hardware specifiche, valuta l'utilizzo di formati di esportazione specializzati come TensorRT per GPU NVIDIA, CoreML per dispositivi Apple o Edge TPU per dispositivi Google Coral.

Quando si esporta un modello YOLO in formati come ONNX o TensorRT, la struttura del tensor di output dipende dal compito del modello. Comprendere questi output è importante per implementazioni di inferenza personalizzate.

Per modelli di detect (ad esempio, yolo26n.pt), l'output è tipicamente un singolo tensor con forma (batch_size, 4 + num_classes, num_predictions) dove i canali rappresentano le coordinate delle box più i punteggi per classe, e num_predictions dipende dalla risoluzione di input dell'esportazione (e può essere dinamico).

Per modelli di segment (ad esempio, yolo26n-seg.pt), si otterranno tipicamente due output: il primo tensor con forma (batch_size, 4 + num_classes + mask_dim, num_predictions) (box, punteggi di classe e coefficienti di maschera), e il secondo tensor con forma (batch_size, mask_dim, proto_h, proto_w) contenente i prototipi di maschera utilizzati con i coefficienti per generare maschere di istanza. Le dimensioni dipendono dalla risoluzione di input dell'esportazione (e possono essere dinamiche).

Per modelli di pose (ad esempio, yolo26n-pose.pt), il tensor di output ha tipicamente forma (batch_size, 4 + num_classes + keypoint_dims, num_predictions), dove keypoint_dims dipende dalla specifica della pose (ad es., numero di keypoint e se la confidenza è inclusa), e num_predictions dipende dalla risoluzione di input dell'esportazione (e può essere dinamico).

Gli esempi negli esempi di inferenza ONNX dimostrano come elaborare questi output per ogni tipo di modello.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load an official model
model = YOLO("path/to/best.pt")  # load a custom-trained model

# Export the model
model.export(format="onnx")
```

Example 2 (unknown):
```unknown
yolo export model=yolo26n.pt format=onnx      # export official model
yolo export model=path/to/best.pt format=onnx # export custom-trained model
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load an official model
model = YOLO("path/to/best.pt")  # load a custom-trained model

# Export the model
model.export(format="onnx")
```

Example 4 (unknown):
```unknown
yolo export model=yolo26n.pt format=onnx      # export official model
yolo export model=path/to/best.pt format=onnx # export custom-trained model
```

---

## Gain Visual Insights with YOLO26's Integration with TensorBoard

**URL:** https://docs.ultralytics.com/integrations/tensorboard/

**Contents:**
- Gain Visual Insights with YOLO26's Integration with TensorBoard
- TensorBoard
- YOLO26 Training with TensorBoard
- Installation
- Configuring TensorBoard for Google Colab
- Usage
- Understanding Your TensorBoard for YOLO26 Training
  - Time Series
    - Key Features of Time Series in TensorBoard
    - Importance of Time Series in YOLO26 Training

Understanding and fine-tuning computer vision models like Ultralytics' YOLO26 becomes more straightforward when you take a closer look at their training processes. Model training visualization helps with getting insights into the model's learning patterns, performance metrics, and overall behavior. YOLO26's integration with TensorBoard makes this process of visualization and analysis easier and enables more efficient and informed adjustments to the model.

This guide covers how to use TensorBoard with YOLO26. You'll learn about various visualizations, from tracking metrics to analyzing model graphs. These tools will help you understand your YOLO26 model's performance better.

TensorBoard, TensorFlow's visualization toolkit, is essential for machine learning experimentation. TensorBoard features a range of visualization tools, crucial for monitoring machine learning models. These tools include tracking key metrics like loss and accuracy, visualizing model graphs, and viewing histograms of weights and biases over time. It also provides capabilities for projecting embeddings to lower-dimensional spaces and displaying multimedia data.

Using TensorBoard while training YOLO26 models is straightforward and offers significant benefits.

To install the required package, run:

TensorBoard is conveniently pre-installed with YOLO26, eliminating the need for additional setup for visualization purposes.

For detailed instructions and best practices related to the installation process, be sure to check our YOLO26 Installation guide. While installing the required packages for YOLO26, if you encounter any difficulties, consult our Common Issues guide for solutions and tips.

When using Google Colab, it's important to set up TensorBoard before starting your training code:

Configure TensorBoard for Google Colab

Before diving into the usage instructions, be sure to check out the range of YOLO26 models offered by Ultralytics. This will help you choose the most appropriate model for your project requirements.

Enable or Disable TensorBoard

By default, TensorBoard logging is disabled. You can enable or disable the logging by using the yolo settings command.

Upon running the usage code snippet above, you can expect the following output:

This output indicates that TensorBoard is now actively monitoring your YOLO26 training session. You can access the TensorBoard dashboard by visiting the provided URL (http://localhost:6006/) to view real-time training metrics and model performance. For users working in Google Colab, the TensorBoard will be displayed in the same cell where you executed the TensorBoard configuration commands.

For more information related to the model training process, be sure to check our YOLO26 Model Training guide. If you are interested in learning more about logging, checkpoints, plotting, and file management, read our usage guide on configuration.

Now, let's focus on understanding the various features and components of TensorBoard in the context of YOLO26 training. The three key sections of the TensorBoard are Time Series, Scalars, and Graphs.

The Time Series feature in the TensorBoard offers a dynamic and detailed perspective of various training metrics over time for YOLO26 models. It focuses on the progression and trends of metrics across training epochs. Here's an example of what you can expect to see.

Filter Tags and Pinned Cards: This functionality allows users to filter specific metrics and pin cards for quick comparison and access. It's particularly useful for focusing on specific aspects of the training process.

Detailed Metric Cards: Time Series divides metrics into different categories like learning rate (lr), training (train), and validation (val) metrics, each represented by individual cards.

Graphical Display: Each card in the Time Series section shows a detailed graph of a specific metric over the course of training. This visual representation aids in identifying trends, patterns, or anomalies in the training process.

In-Depth Analysis: Time Series provides an in-depth analysis of each metric. For instance, different learning rate segments are shown, offering insights into how adjustments in learning rate impact the model's learning curve.

The Time Series section is essential for a thorough analysis of the YOLO26 model's training progress. It lets you track the metrics in real time to promptly identify and solve issues. It also offers a detailed view of each metric's progression, which is crucial for fine-tuning the model and enhancing its performance.

Scalars in the TensorBoard are crucial for plotting and analyzing simple metrics like loss and accuracy during the training of YOLO26 models. They offer a clear and concise view of how these metrics evolve with each training epoch, providing insights into the model's learning effectiveness and stability. Here's an example of what you can expect to see.

Learning Rate (lr) Tags: These tags show the variations in the learning rate across different segments (e.g., pg0, pg1, pg2). This helps us understand the impact of learning rate adjustments on the training process.

Metrics Tags: Scalars include performance indicators such as:

mAP50 (B): Mean Average Precision at 50% Intersection over Union (IoU), crucial for assessing object detection accuracy.

mAP50-95 (B): Mean Average Precision calculated over a range of IoU thresholds, offering a more comprehensive evaluation of accuracy.

Precision (B): Indicates the ratio of correctly predicted positive observations, key to understanding prediction accuracy.

Recall (B): Important for models where missing a detection is significant, this metric measures the ability to detect all relevant instances.

To learn more about the different metrics, read our guide on performance metrics.

Training and Validation Tags (train, val): These tags display metrics specifically for the training and validation datasets, allowing for a comparative analysis of model performance across different data sets.

Observing scalar metrics is crucial for fine-tuning the YOLO26 model. Variations in these metrics, such as spikes or irregular patterns in loss graphs, can highlight potential issues such as overfitting, underfitting, or inappropriate learning rate settings. By closely monitoring these scalars, you can make informed decisions to optimize the training process, ensuring that the model learns effectively and achieves the desired performance.

While both Scalars and Time Series in TensorBoard are used for tracking metrics, they serve slightly different purposes. Scalars focus on plotting simple metrics such as loss and accuracy as scalar values. They provide a high-level overview of how these metrics change with each training epoch. Meanwhile, the time-series section of the TensorBoard offers a more detailed timeline view of various metrics. It is particularly useful for monitoring the progression and trends of metrics over time, providing a deeper dive into the specifics of the training process.

The Graphs section of the TensorBoard visualizes the computational graph of the YOLO26 model, showing how operations and data flow within the model. It's a powerful tool for understanding the model's structure, ensuring that all layers are connected correctly, and for identifying any potential bottlenecks in data flow. Here's an example of what you can expect to see.

Graphs are particularly useful for debugging the model, especially in complex architectures typical in deep learning models like YOLO26. They help in verifying layer connections and the overall design of the model.

This guide aims to help you use TensorBoard with YOLO26 for visualization and analysis of machine learning model training. It focuses on explaining how key TensorBoard features can provide insights into training metrics and model performance during YOLO26 training sessions.

For a more detailed exploration of these features and effective utilization strategies, you can refer to TensorFlow's official TensorBoard documentation and their GitHub repository.

Want to learn more about the various integrations of Ultralytics? Check out the Ultralytics integrations guide page to see what other exciting capabilities are waiting to be discovered!

Using TensorBoard with YOLO26 provides several visualization tools essential for efficient model training:

These tools enable you to make informed adjustments to enhance your YOLO26 model's performance. For more details on TensorBoard features, check out the TensorFlow TensorBoard guide.

To monitor training metrics while training a YOLO26 model with TensorBoard, follow these steps:

The TensorBoard dashboard, accessible via http://localhost:6006/, provides real-time insights into various training metrics. For a deeper dive into training configurations, visit our YOLO26 Configuration guide.

When training YOLO26 models, TensorBoard allows you to visualize an array of important metrics including:

These visualizations are essential for tracking model performance and making necessary optimizations. For more information on these metrics, refer to our Performance Metrics guide.

Yes, you can use TensorBoard in a Google Colab environment to train YOLO26 models. Here's a quick setup:

Configure TensorBoard for Google Colab

Then, run the YOLO26 training script:

TensorBoard will visualize the training progress within Colab, providing real-time insights into metrics like loss and accuracy. For additional details on configuring YOLO26 training, see our detailed YOLO26 Installation guide.

**Examples:**

Example 1 (go):
```go
# Install the required package for YOLO26 and Tensorboard
pip install ultralytics
```

Example 2 (unknown):
```unknown
%load_ext tensorboard
%tensorboard --logdir path/to/runs
```

Example 3 (markdown):
```markdown
# Enable TensorBoard logging
yolo settings tensorboard=True

# Disable TensorBoard logging
yolo settings tensorboard=False
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a pretrained model
model = YOLO("yolo26n.pt")

# Train the model
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

---

## Home

**URL:** https://docs.ultralytics.com/it/

**Contents:**
- Home
- Da dove iniziare
- YOLO: Breve storia
- Licenze YOLO: come viene concesso in licenza Ultralytics YOLO?
- L'evoluzione dell'object detection
- FAQ
  - Cos'è Ultralytics YOLO e come migliora il rilevamento degli oggetti?
  - Come posso iniziare con l'installazione e la configurazione di YOLO?
  - Come posso addestrare un modello YOLO personalizzato sul mio set di dati?
  - Quali sono le opzioni di licenza disponibili per Ultralytics YOLO?

Presentiamo Ultralytics YOLO26, l'ultima versione dell'acclamato modello di rilevamento di oggetti in tempo reale e segmentazione delle immagini. YOLO26 si basa sui progressi del deep learning e della visione artificiale, offrendo inferenza end-to-end NMS-free e deployment ottimizzato per edge. Il suo design semplificato lo rende adatto a varie applicazioni e facilmente adattabile a diverse piattaforme hardware, dai dispositivi edge alle API cloud. Per carichi di lavoro di produzione stabili, sono raccomandati sia YOLO26 che YOLO11.

Esplora la documentazione di Ultralytics, una risorsa completa progettata per aiutarti a comprendere e utilizzare le sue caratteristiche e capacità. Che tu sia un professionista esperto nel machine learning o un nuovo arrivato nel campo, questo hub mira a massimizzare il potenziale di YOLO nei tuoi progetti.

Installa ultralytics con pip e inizia in pochi minuti ad addestrare un modello YOLO

Esegui previsioni su nuove immagini, video e stream con YOLO

Addestra un nuovo modello YOLO sul tuo dataset personalizzato da zero oppure carica e addestra su un modello pre-addestrato

Esplora le attività di Computer Vision

Scopri le attività YOLO come detect, segment, classify, pose, OBB e track

Esplora YOLO26 🚀 NOVITÀ

Scopri gli ultimi modelli YOLO26 di Ultralytics con inferenza NMS-free e ottimizzazione per edge

SAM 3: Segment Anything con Concetti 🚀 NOVITÀ

L'ultimo SAM 3 di Meta con Segmentazione di Concetti Promptable - segment tutte le istanze utilizzando testo o esemplari di immagini

Open Source, AGPL-3.0

Ultralytics offre due licenze YOLO: AGPL-3.0 ed Enterprise. Esplora YOLO su GitHub.

Guarda: Come addestrare un modello YOLO11 sul tuo set di dati personalizzato in Google Colab.

YOLO (You Only Look Once), un popolare modello di object detection e image segmentation, è stato sviluppato da Joseph Redmon e Ali Farhadi presso l'Università di Washington. Lanciato nel 2015, YOLO ha guadagnato popolarità per la sua alta velocità e precisione.

Ultralytics offre due opzioni di licenza per soddisfare diversi casi d'uso:

La nostra strategia di licenza è progettata per garantire che qualsiasi miglioramento ai nostri progetti open-source venga restituito alla comunità. Crediamo nell'open source e la nostra missione è garantire che i nostri contributi possano essere utilizzati ed espansi in modi che beneficino tutti.

Il rilevamento di oggetti si è evoluto significativamente nel corso degli anni, dalle tradizionali tecniche di computer vision ai modelli avanzati di deep learning. La famiglia di modelli YOLO è stata in prima linea in questa evoluzione, spingendo costantemente i confini di ciò che è possibile nel rilevamento di oggetti in tempo reale.

L'approccio unico di YOLO considera il rilevamento degli oggetti come un singolo problema di regressione, prevedendo bounding box e probabilità di classe direttamente dalle immagini complete in una singola valutazione. Questo metodo rivoluzionario ha reso i modelli YOLO significativamente più veloci rispetto ai precedenti rilevatori a due stadi, pur mantenendo un'elevata accuratezza.

Con ogni nuova versione, YOLO ha introdotto miglioramenti architetturali e tecniche innovative che hanno migliorato le prestazioni su varie metriche. YOLO26 continua questa tradizione incorporando gli ultimi progressi nella ricerca sulla visione artificiale, con inferenza end-to-end NMS-free e deployment ottimizzato per edge per applicazioni nel mondo reale.

Ultralytics YOLO è l'acclamata serie YOLO (You Only Look Once) per il rilevamento di oggetti in tempo reale e la segmentazione delle immagini. L'ultimo modello, YOLO26, si basa sulle versioni precedenti introducendo l'inferenza end-to-end NMS-free e il deployment ottimizzato per edge. YOLO supporta varie attività di visione AI come detect, segment, stima della posa, track e classificazione. La sua architettura efficiente garantisce velocità e accuratezza eccellenti, rendendolo adatto a diverse applicazioni, inclusi dispositivi edge e API cloud.

Iniziare con YOLO è semplice e veloce. Puoi installare il pacchetto Ultralytics usando pip ed essere operativo in pochi minuti. Ecco un comando di installazione di base:

Installazione tramite pip

Per una guida completa dettagliata, visita la nostra pagina di Avvio rapido. Questa risorsa ti aiuterà con le istruzioni di installazione, la configurazione iniziale e l'esecuzione del tuo primo modello.

L'addestramento di un modello YOLO personalizzato sul tuo set di dati prevede alcuni passaggi dettagliati:

Ecco un codice di esempio per l'attività di rilevamento oggetti:

Esempio di addestramento per l'attività di rilevamento oggetti

Per una guida dettagliata, consulta la nostra guida Addestra un modello, che include esempi e suggerimenti per ottimizzare il processo di addestramento.

Ultralytics offre due opzioni di licenza per YOLO:

Per maggiori dettagli, visita la nostra pagina Licenze.

Ultralytics YOLO supporta il tracciamento multi-oggetto efficiente e personalizzabile. Per utilizzare le funzionalità di tracciamento, puoi utilizzare il yolo track comando, come mostrato di seguito:

Esempio per il tracciamento di oggetti su un video

Per una guida dettagliata sulla configurazione e l'esecuzione del tracciamento degli oggetti, consulta la nostra documentazione sulla Modalità Track, che spiega la configurazione e le applicazioni pratiche in scenari in tempo reale.

**Examples:**

Example 1 (unknown):
```unknown
pip install -U ultralytics
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a pretrained YOLO model (you can choose n, s, m, l, or x versions)
model = YOLO("yolo26n.pt")

# Start training on your custom dataset
model.train(data="path/to/dataset.yaml", epochs=100, imgsz=640)
```

Example 3 (sql):
```sql
# Train a YOLO model from the command line
yolo detect train data=path/to/dataset.yaml epochs=100 imgsz=640
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a pretrained YOLO model
model = YOLO("yolo26n.pt")

# Start tracking objects in a video
# You can also use live video streams or webcam input
model.track(source="path/to/video.mp4")
```

---

## Installa Ultralytics

**URL:** https://docs.ultralytics.com/it/quickstart/

**Contents:**
- Installa Ultralytics
  - Immagine Docker Conda
- Installazione su server headless
- Installazione avanzata
- Usa Ultralytics con la CLI
- Usa Ultralytics con Python
- Impostazioni di Ultralytics
  - Ispezione delle impostazioni
  - Modifica delle impostazioni
  - Comprensione delle impostazioni

Ultralytics offre una varietà di metodi di installazione, tra cui pip, conda e Docker. Puoi installare YOLO tramite ultralytics pacchetto pip per l'ultima release stabile, oppure clonando il repository GitHub di Ultralytics per la versione più recente. Docker è anche un'opzione per eseguire il pacchetto in un container isolato, il che evita l'installazione locale.

Guarda: Guida rapida di Ultralytics YOLO

Installa o aggiorna il ultralytics package usando pip eseguendo pip install -U ultralytics. Per maggiori dettagli sul ultralytics package, visita il Python Package Index (PyPI).

È anche possibile installare ultralytics direttamente dalla repository GitHub di Ultralytics. Questo può essere utile se desideri l'ultima versione di sviluppo. Assicurati di avere lo strumento da riga di comando Git installato, quindi esegui:

Conda può essere utilizzato come gestore di pacchetti alternativo a pip. Per maggiori dettagli, visita Anaconda. Il repository di feedstock di Ultralytics per l'aggiornamento del pacchetto conda è disponibile su GitHub.

Se stai eseguendo l'installazione in un ambiente CUDA, è consigliabile installare ultralytics, pytorch, e pytorch-cuda nello stesso comando. Ciò consente al gestore di pacchetti conda di risolvere eventuali conflitti. In alternativa, installa pytorch-cuda ultimo per sovrascrivere quello specifico della CPU pytorch specifico per la CPU, se necessario.

Le immagini Docker di Ultralytics Conda sono disponibili anche su Docker Hub. Queste immagini sono basate su Miniconda3 e forniscono un modo semplice per iniziare a utilizzare ultralytics in un ambiente Conda.

Clona il repository repository GitHub di Ultralytics se sei interessato a contribuire allo sviluppo o desideri sperimentare con il codice sorgente più recente. Dopo aver clonato, accedi alla directory e installa il pacchetto in modalità modificabile -e utilizzando pip.

Utilizza Docker per eseguire il ultralytics package in un container isolato, garantendo prestazioni coerenti in vari ambienti. Selezionando uno degli ufficiali ultralytics da Docker Hub, si evita la complessità dell'installazione locale e si ottiene l'accesso a un ambiente di lavoro verificato. Ultralytics offre cinque immagini Docker principali supportate, ciascuna progettata per un'elevata compatibilità ed efficienza:

Ecco i comandi per ottenere l'immagine più recente ed eseguirla:

Il comando sopra riportato inizializza un container Docker con l'ultima ultralytics immagine. Il flag -it flags assegnano uno pseudo-TTY e mantengono aperto stdin, consentendo l'interazione con il container. Il --ipc=host imposta il namespace IPC (Inter-Process Communication) sull'host, essenziale per la condivisione della memoria tra i processi. Il flag --gpus all flag abilita l'accesso a tutte le GPU disponibili all'interno del container, fondamentale per le attività che richiedono calcolo tramite GPU.

Nota: Per lavorare con i file sulla tua macchina locale all'interno del container, usa i volumi Docker per montare una directory locale nel container:

Sostituisci /path/on/host con il percorso della directory sulla macchina locale e /path/in/container con il percorso desiderato all'interno del container Docker.

Per un utilizzo avanzato di Docker, esplora la Guida a Docker di Ultralytics.

Vedere il file ultralytics pyproject.toml per un elenco delle dipendenze. Si noti che tutti gli esempi precedenti installano tutte le dipendenze richieste.

I requisiti di PyTorch variano in base al sistema operativo e ai requisiti CUDA, quindi installa prima PyTorch seguendo le istruzioni su PyTorch.

Per ambienti server senza display (ad es. VM cloud, container Docker, pipeline CI/CD), utilizzare il ultralytics-opencv-headless pacchetto. Questo è identico allo standard ultralytics pacchetto ma dipende da opencv-python-headless invece di opencv-python, evitando dipendenze GUI non necessarie e potenziali libGL errori.

Installazione Headless

Entrambi i pacchetti offrono la stessa funzionalità e API. La variante headless esclude semplicemente i componenti GUI di OpenCV che richiedono librerie di visualizzazione.

Sebbene i metodi di installazione standard coprano la maggior parte dei casi d'uso, potresti aver bisogno di una configurazione più personalizzata per lo sviluppo o per configurazioni ad hoc.

Se hai bisogno di modifiche personalizzate persistenti, puoi effettuare un fork del repository Ultralytics, apportare modifiche a pyproject.toml o altro codice, e installa dal tuo fork.

Clona il repository localmente, modifica i file secondo necessità e installa in modalità modificabile.

Questo approccio è utile per lo sviluppo o il test di modifiche locali prima del commit.

Specifica un fork personalizzato di Ultralytics nel tuo requirements.txt file per garantire installazioni coerenti all'interno del tuo team.

Installa le dipendenze dal file:

L'interfaccia a riga di comando (CLI) di Ultralytics consente semplici comandi a riga singola senza la necessità di un ambiente Python. La CLI non richiede personalizzazioni o codice Python; esegui tutte le attività dal terminale con il yolo comando. Per maggiori informazioni sull'utilizzo di YOLO dalla riga di comando, consultare la Guida CLI.

Ultralytics yolo i comandi utilizzano la seguente sintassi:

Vedi tutti i ARGS nel completo Guida alla Configurazione o con il comando yolo cfg CLI.

Addestra un modello di rilevamento per 10 epoche con un tasso di apprendimento iniziale di 0.01:

Esegui una prediction su un video di YouTube utilizzando un modello di segmentazione pre-addestrato con una dimensione dell'immagine di 320:

Convalida di un modello di rilevamento pre-addestrato con una dimensione del batch di 1 e una dimensione dell'immagine di 640:

Esporta un modello di classificazione YOLO26n in formato ONNX con una dimensione dell'immagine di 224x128 (nessun TASK richiesto):

Conta gli oggetti in un video o in uno streaming live usando YOLO26:

Monitora gli esercizi di allenamento usando un modello di posa YOLO26:

Usa YOLO26 per contare gli oggetti in una coda o regione designata:

Esegui il rilevamento di oggetti, la segmentazione di istanze o la stima della posa in un browser web utilizzando Streamlit:

Esegui comandi speciali per visualizzare la versione, le impostazioni, eseguire controlli e altro:

Gli argomenti devono essere passati come arg=value coppie, separate da un segno di uguale = segno e delimitato da spazi. Non utilizzare -- o virgole per gli argomenti , tra gli argomenti.

L'interfaccia Python di YOLO di Ultralytics offre una perfetta integrazione nei progetti Python, semplificando il caricamento, l'esecuzione e l'elaborazione degli output del modello. Progettata per la semplicità, l'interfaccia Python consente agli utenti di implementare rapidamente object detection, segmentation e classification. Questo rende l'interfaccia Python di YOLO uno strumento prezioso per incorporare queste funzionalità nei progetti Python.

Ad esempio, gli utenti possono caricare un modello, addestrarlo, valutarne le prestazioni ed esportarlo in formato ONNX con poche righe di codice. Consulta la Guida Python per saperne di più sull'utilizzo di YOLO all'interno dei tuoi progetti Python.

La libreria Ultralytics include un SettingsManager per un controllo preciso sugli esperimenti, consentendo agli utenti di accedere e modificare facilmente le impostazioni. Memorizzate in un file JSON all'interno della directory di configurazione utente dell'ambiente, queste impostazioni possono essere visualizzate o modificate nell'ambiente Python o tramite l'interfaccia a riga di comando (CLI).

Per visualizzare la configurazione corrente delle impostazioni:

Visualizza impostazioni

Utilizza python per visualizzare le tue impostazioni importando il settings oggetto dal ultralytics modulo. Stampa e restituisci le impostazioni con questi comandi:

L'interfaccia a riga di comando consente di verificare le impostazioni con:

Ultralytics semplifica la modifica delle impostazioni nei seguenti modi:

Aggiorna impostazioni

In Python, usa il update metodo sull'oggetto settings object:

Per modificare le impostazioni usando l'interfaccia a riga di comando:

La tabella seguente fornisce una panoramica delle impostazioni regolabili all'interno di Ultralytics, inclusi valori di esempio, tipi di dati e descrizioni.

Rivedi queste impostazioni man mano che avanzi nei progetti o negli esperimenti per garantire una configurazione ottimale.

Installa Ultralytics con pip usando:

Questo installa l'ultima versione stabile del ultralytics pacchetto da PyPI. Per installare la versione di sviluppo direttamente da GitHub:

Assicurati che lo strumento da riga di comando Git sia installato sul tuo sistema.

Sì, installa Ultralytics YOLO usando conda con:

Questo metodo è un'ottima alternativa a pip, garantendo la compatibilità con altri pacchetti. Per gli ambienti CUDA, installa ultralytics, pytorch, e pytorch-cuda insieme per risolvere i conflitti:

Per maggiori istruzioni, consultare la guida rapida di Conda.

Docker fornisce un ambiente isolato e coerente per Ultralytics YOLO, garantendo prestazioni fluide tra i sistemi ed evitando complessità di installazione locale. Le immagini Docker ufficiali sono disponibili su Docker Hub, con varianti per GPU, CPU, ARM64, NVIDIA Jetson e Conda. Per scaricare ed eseguire l'immagine più recente:

Per istruzioni dettagliate su Docker, consulta la guida rapida di Docker.

Clona il repository Ultralytics e configura un ambiente di sviluppo con:

Ciò consente di contribuire al progetto o di sperimentare con il codice sorgente più recente. Per i dettagli, visitare il repository GitHub di Ultralytics.

La CLI YOLO di Ultralytics semplifica l'esecuzione di attività di object detection senza codice Python, consentendo comandi a riga singola per training, convalida e previsione direttamente dal tuo terminale. La sintassi di base è:

Ad esempio, per addestrare un modello di rilevamento:

Esplora altri comandi ed esempi di utilizzo nella Guida CLI completa.

**Examples:**

Example 1 (go):
```go
# Install or upgrade the ultralytics package from PyPI
pip install -U ultralytics
```

Example 2 (swift):
```swift
# Install the ultralytics package from GitHub
pip install git+https://github.com/ultralytics/ultralytics.git@main
```

Example 3 (go):
```go
# Install the ultralytics package using conda
conda install -c conda-forge ultralytics
```

Example 4 (julia):
```julia
# Install all packages together using conda
conda install -c pytorch -c nvidia -c conda-forge pytorch torchvision pytorch-cuda=11.8 ultralytics
```

---

## Integrazioni Ultralytics

**URL:** https://docs.ultralytics.com/it/integrations/

**Contents:**
- Integrazioni Ultralytics
- Integrazioni per il training
- Integrazioni per il deployment
- Integrazioni di dataset
  - Formati di esportazione
- Contribuisci alle nostre integrazioni
- FAQ
  - Cos'è Ultralytics Platform e come semplifica il flusso di lavoro ML?
  - Posso monitorare le prestazioni dei miei modelli Ultralytics utilizzando MLFlow?
  - Quali sono i vantaggi dell'utilizzo di Neural Magic per l'ottimizzazione dei modelli YOLO26?

Benvenuti nella pagina delle integrazioni di Ultralytics! Questa pagina fornisce una panoramica delle nostre partnership con vari strumenti e piattaforme, progettate per semplificare i tuoi flussi di lavoro di machine learning, migliorare la gestione dei dataset, semplificare il training dei modelli e facilitare un deployment efficiente.

Guarda: Ultralytics YOLO Deployment e Integrazioni

Albumentations: Migliora i tuoi modelli Ultralytics con potenti aumenti di immagini per migliorare la robustezza e la generalizzazione del modello.

Amazon SageMaker: Sfrutta Amazon SageMaker per costruire, addestrare e distribuire in modo efficiente i modelli Ultralytics, fornendo una piattaforma all-in-one per il ciclo di vita dell'ML.

ClearML: Automatizza i tuoi flussi di lavoro ML di Ultralytics, monitora gli esperimenti e promuovi la collaborazione del team.

Comet ML: Migliora lo sviluppo del tuo modello con Ultralytics tracciando, confrontando e ottimizzando i tuoi esperimenti di machine learning.

DVC: Implementa il controllo della versione per i tuoi progetti di machine learning Ultralytics, sincronizzando efficacemente dati, codice e modelli.

Google Colab: Utilizza Google Colab per addestrare e valutare i modelli Ultralytics in un ambiente basato su cloud che supporta la collaborazione e la condivisione.

IBM Watsonx: Scopri come IBM Watsonx semplifica l'addestramento e la valutazione dei modelli Ultralytics con i suoi strumenti di intelligenza artificiale all'avanguardia, l'integrazione semplice e il sistema avanzato di gestione dei modelli.

JupyterLab: Scopri come utilizzare l'ambiente interattivo e personalizzabile di JupyterLab per addestrare e valutare i modelli Ultralytics con facilità ed efficienza.

Kaggle: Esplora come puoi utilizzare Kaggle per addestrare e valutare i modelli Ultralytics in un ambiente basato su cloud con librerie preinstallate, supporto GPU e una vivace comunità per la collaborazione e la condivisione.

MLFlow: Semplifica l'intero ciclo di vita ML dei modelli Ultralytics, dalla sperimentazione e riproducibilità al deployment.

Neptune: Mantieni un registro completo dei tuoi esperimenti di ML con Ultralytics in questo archivio di metadati progettato per MLOps.

Paperspace Gradient: Paperspace Gradient semplifica il lavoro sui progetti YOLO26 fornendo strumenti cloud facili da usare per addestrare, testare e distribuire rapidamente i tuoi modelli.

Ray Tune: Ottimizza gli iperparametri dei tuoi modelli Ultralytics su qualsiasi scala.

TensorBoard: Visualizza i tuoi flussi di lavoro ML di Ultralytics, monitora le metriche del modello e promuovi la collaborazione del team.

Ultralytics Platform: Accedi e contribuisci a una community di modelli Ultralytics pre-addestrati.

VS Code: Un'estensione per VS Code che fornisce frammenti di codice per accelerare i flussi di lavoro di sviluppo di Ultralytics e offre esempi per aiutare chiunque a imparare o iniziare.

Weights & Biases (W&B): Monitora gli esperimenti, visualizza le metriche e promuovi la riproducibilità e la collaborazione sui progetti Ultralytics.

Axelera: Esplora gli acceleratori Metis e l'SDK Voyager per eseguire modelli Ultralytics con un'efficiente inference edge.

CoreML: CoreML, sviluppato da Apple, è un framework progettato per integrare in modo efficiente i modelli di machine learning nelle applicazioni su iOS, macOS, watchOS e tvOS, utilizzando l'hardware di Apple per una distribuzione del modello efficace e sicura.

ExecuTorch: Sviluppato da Meta, ExecuTorch è la soluzione unificata di PyTorch per il deployment dei modelli Ultralytics YOLO su dispositivi edge.

Gradio: Distribuisci i modelli Ultralytics con Gradio per demo interattive di object detection in tempo reale.

MNN: Sviluppato da Alibaba, MNN è un framework di deep learning altamente efficiente e leggero. Supporta l'inferenza e l'addestramento di modelli di deep learning e offre prestazioni leader del settore per l'inferenza e l'addestramento on-device.

NCNN: Sviluppato da Tencent, NCNN è un framework di inferenza di reti neurali efficiente, progettato per dispositivi mobili. Consente la distribuzione diretta di modelli AI nelle app, ottimizzando le prestazioni su varie piattaforme mobili.

Neural Magic: Sfrutta le tecniche di Quantization Aware Training (QAT) e pruning per ottimizzare i modelli Ultralytics per prestazioni superiori e dimensioni più snelle.

ONNX: Un formato open-source creato da Microsoft per facilitare il trasferimento di modelli AI tra vari framework, migliorando la versatilità e la flessibilità di distribuzione dei modelli Ultralytics.

OpenVINO: Il toolkit di Intel per ottimizzare e distribuire in modo efficiente i modelli di computer vision su varie piattaforme Intel CPU e GPU.

PaddlePaddle: Una piattaforma di deep learning open-source di Baidu, PaddlePaddle consente la distribuzione efficiente di modelli AI e si concentra sulla scalabilità delle applicazioni industriali.

Rockchip RKNN: Sviluppato da Rockchip, RKNN è un framework di inferenza di rete neurale specializzato, ottimizzato per le piattaforme hardware di Rockchip, in particolare le loro NPU. Facilita l'implementazione efficiente di modelli di IA su dispositivi edge, consentendo un'inferenza ad alte prestazioni in applicazioni in tempo reale.

Seeed Studio reCamera: Sviluppata da Seeed Studio, reCamera è un dispositivo AI edge avanzato progettato per applicazioni di computer vision in tempo reale. Alimentato dal processore SG200X basato su RISC-V, offre inferenza AI ad alte prestazioni con efficienza energetica. Il suo design modulare, le capacità avanzate di elaborazione video e il supporto per un'implementazione flessibile lo rendono una scelta ideale per vari casi d'uso, tra cui il monitoraggio della sicurezza, le applicazioni ambientali e la produzione.

SONY IMX500: Ottimizza e distribuisci modelli Ultralytics YOLO26 su fotocamere AI Raspberry Pi con il sensore IMX500 per prestazioni veloci e a basso consumo.

TensorRT: Sviluppato da NVIDIA, questo framework di inferenza di deep learning ad alte prestazioni e formato di modello ottimizza i modelli AI per velocità ed efficienza accelerate sulle GPU NVIDIA, garantendo una distribuzione semplificata.

TF GraphDef: Sviluppato da Google, GraphDef è il formato di TensorFlow per rappresentare grafi di calcolo, consentendo l'esecuzione ottimizzata di modelli di machine learning su hardware diversi.

TF SavedModel: Sviluppato da Google, TF SavedModel è un formato di serializzazione universale per i modelli TensorFlow, che consente una facile condivisione e distribuzione su una vasta gamma di piattaforme, dai server ai dispositivi edge.

TF.js: Sviluppato da Google per facilitare il machine learning nei browser e in Node.js, TF.js consente la distribuzione di modelli ML basati su JavaScript.

TFLite: Sviluppato da Google, TFLite è un framework leggero per l'implementazione di modelli di machine learning su dispositivi mobili ed edge, garantendo un'inferenza rapida ed efficiente con un ingombro di memoria minimo.

TFLite Edge TPU: Sviluppato da Google per l'ottimizzazione dei modelli TensorFlow Lite su Edge TPU, questo formato di modello garantisce un edge computing efficiente e ad alta velocità.

TorchScript: Sviluppato come parte del framework PyTorch, TorchScript consente l'esecuzione e la distribuzione efficiente di modelli di machine learning in vari ambienti di produzione senza la necessità di dipendenze Python.

Supportiamo anche una varietà di formati di esportazione dei modelli per la distribuzione in diversi ambienti. Ecco i formati disponibili:

Consulta i link per saperne di più su ciascuna integrazione e su come sfruttarle al meglio con Ultralytics. Vedi la export dettagli nella Esportazione pagina.

Siamo sempre entusiasti di vedere come la comunità integra Ultralytics YOLO con altre tecnologie, strumenti e piattaforme! Se hai integrato con successo YOLO con un nuovo sistema o hai preziose informazioni da condividere, considera di contribuire alla nostra documentazione sulle integrazioni.

Scrivendo una guida o un tutorial, puoi contribuire ad ampliare la nostra documentazione e fornire esempi reali a vantaggio della community. È un modo eccellente per contribuire al crescente ecosistema intorno a Ultralytics YOLO.

Per contribuire, consulta la nostra Guida per i contributori per istruzioni su come inviare una Pull Request (PR) 🛠️. Attendiamo con impazienza i tuoi contributi!

Collaboriamo per rendere l'ecosistema Ultralytics YOLO più ampio e ricco di funzionalità 🙏!

Ultralytics Platform è una piattaforma basata su cloud progettata per rendere i flussi di lavoro di machine learning per i modelli Ultralytics fluidi ed efficienti. Utilizzando questo strumento, puoi facilmente caricare dataset, addestrare modelli, eseguire il track in tempo reale e distribuire modelli YOLO senza la necessità di ampie competenze di codifica. La piattaforma funge da spazio di lavoro centralizzato dove puoi gestire l'intera pipeline ML dalla preparazione dei dati alla distribuzione. Puoi esplorare le funzionalità chiave sulla pagina Ultralytics Platform e iniziare rapidamente con la nostra guida Quickstart.

Sì, puoi. L'integrazione di MLFlow con i modelli Ultralytics ti consente di track gli esperimenti, migliorare la riproducibilità e semplificare l'intero ciclo di vita dell'ML. Istruzioni dettagliate per l'impostazione di questa integrazione sono disponibili nella pagina di integrazione MLFlow. Questa integrazione è particolarmente utile per monitorare le metriche del modello, confrontare diverse esecuzioni di addestramento e gestire in modo efficiente il flusso di lavoro dell'ML. MLFlow fornisce una piattaforma centralizzata per registrare parametri, metriche e artefatti, rendendo più facile comprendere il comportamento del modello e apportare miglioramenti basati sui dati.

Neural Magic ottimizza i modelli YOLO26 sfruttando tecniche come il Quantization Aware Training (QAT) e il pruning, ottenendo modelli altamente efficienti e più piccoli che offrono prestazioni migliori su hardware con risorse limitate. Consulta la pagina di integrazione di Neural Magic per scoprire come implementare queste ottimizzazioni per prestazioni superiori e modelli più snelli. Ciò è particolarmente vantaggioso per la distribuzione su dispositivi edge dove le risorse computazionali sono limitate. Il motore DeepSparse di Neural Magic può offrire un'inferenza fino a 6 volte più veloce sulle CPU, rendendo possibile l'esecuzione di modelli complessi senza hardware specializzato.

Per distribuire i modelli Ultralytics YOLO con Gradio per demo interattive di object detection, puoi seguire i passaggi descritti nella pagina di integrazione di Gradio. Gradio ti consente di creare interfacce web facili da usare per l'inferenza del modello in tempo reale, rendendolo uno strumento eccellente per mostrare le capacità del tuo modello YOLO in un formato intuitivo adatto sia agli sviluppatori che agli utenti finali. Con poche righe di codice, puoi creare applicazioni interattive che dimostrano le prestazioni del tuo modello su input personalizzati, facilitando una migliore comprensione e valutazione delle tue soluzioni di computer vision.

---

## Live Inference with Streamlit Application using Ultralytics YOLO26

**URL:** https://docs.ultralytics.com/guides/streamlit-live-inference/

**Contents:**
- Live Inference with Streamlit Application using Ultralytics YOLO26
- Introduction
- Advantages of Live Inference
- Streamlit Application Code
- How It Works
- Conclusion
- Share Your Thoughts with the Community
  - Where to Find Help and Support
  - Official Documentation
- FAQ

Streamlit makes it simple to build and deploy interactive web applications. Combining this with Ultralytics YOLO26 allows for real-time object detection and analysis directly in your browser. YOLO26's high accuracy and speed ensure seamless performance for live video streams, making it ideal for applications in security, retail, and beyond.

Watch: How to Use Streamlit with Ultralytics for Real-Time Computer Vision in Your Browser

Ultralytics Installation

Before you start building the application, ensure you have the Ultralytics Python package installed.

Inference using Streamlit with Ultralytics YOLO

These commands launch the default Streamlit interface that ships with Ultralytics. Use yolo solutions inference --help to view additional flags such as source, conf, or persist if you want to customize the experience without editing Python code.

This will launch the Streamlit application in your default web browser. You will see the main title, subtitle, and the sidebar with configuration options. Select your desired YOLO26 model, set the confidence and NMS thresholds, and click the "Start" button to begin the real-time object detection.

Under the hood, the Streamlit application uses the Ultralytics solutions module to create an interactive interface. When you start the inference, the application:

The application provides a clean, user-friendly interface with controls to adjust model parameters and start/stop inference at any time.

By following this guide, you have successfully created a real-time object detection application using Streamlit and Ultralytics YOLO26. This application allows you to experience the power of YOLO26 in detecting objects through your webcam, with a user-friendly interface and the ability to stop the video stream at any time.

For further enhancements, you can explore adding more features such as recording the video stream, saving the annotated frames, or integrating with other computer vision libraries.

Engage with the community to learn more, troubleshoot issues, and share your projects:

Setting up a real-time object detection application with Streamlit and Ultralytics YOLO26 is straightforward. First, ensure you have the Ultralytics Python package installed using:

Then, you can create a basic Streamlit application to run live inference:

Streamlit Application

For more details on the practical setup, refer to the Streamlit Application Code section of the documentation.

Using Ultralytics YOLO26 with Streamlit for real-time object detection offers several advantages:

Learn more about these benefits in the Advantages of Live Inference section.

After coding your Streamlit application integrating Ultralytics YOLO26, you can deploy it by running:

This command will launch the application in your default web browser, enabling you to select YOLO26 models, set confidence and NMS thresholds, and start real-time object detection with a simple click. For a detailed guide, refer to the Streamlit Application Code section.

Real-time object detection using Streamlit and Ultralytics YOLO26 can be applied in various sectors:

For more in-depth use cases and examples, explore Ultralytics Solutions.

Ultralytics YOLO26 provides several enhancements over prior models like YOLOv5 and RCNNs:

For a comprehensive comparison, check Ultralytics YOLO26 Documentation and related blog posts discussing model performance.

**Examples:**

Example 1 (unknown):
```unknown
pip install ultralytics
```

Example 2 (unknown):
```unknown
yolo solutions inference

yolo solutions inference model="path/to/model.pt"
```

Example 3 (python):
```python
from ultralytics import solutions

inf = solutions.Inference(
    model="yolo26n.pt",  # you can use any model that Ultralytics supports, e.g., YOLO26, or a custom-trained model
)

inf.inference()

# Make sure to run the file using command `streamlit run path/to/file.py`
```

Example 4 (unknown):
```unknown
pip install ultralytics
```

---

## Modalità Ultralytics YOLO26

**URL:** https://docs.ultralytics.com/it/modes/

**Contents:**
- Modalità Ultralytics YOLO26
- Introduzione
  - Modalità in sintesi
- Addestramento
- Valutazione
- Predizione
- Esportazione
- Tracciamento
- Benchmark
- FAQ

Ultralytics YOLO26 non è solo un altro modello di object detect; è un framework versatile progettato per coprire l'intero ciclo di vita dei modelli di machine learning—dall'acquisizione dei dati e l'addestramento del modello alla validazione, al deployment e al tracking nel mondo reale. Ogni modalità serve a uno scopo specifico ed è progettata per offrire la flessibilità e l'efficienza richieste per diverse attività e casi d'uso.

Guarda: Tutorial sulle modalità di Ultralytics: addestramento, convalida, previsione, esportazione e benchmark.

Comprendere le diverse modalità supportate da Ultralytics YOLO26 è fondamentale per ottenere il massimo dai tuoi modelli:

Questa guida completa mira a fornire una panoramica e approfondimenti pratici su ogni modalità, aiutandoti a sfruttare appieno il potenziale di YOLO26.

La modalità Train viene utilizzata per addestrare un modello YOLO26 su un dataset custom. In questa modalità, il modello viene addestrato utilizzando il dataset e gli iperparametri specificati. Il processo di addestramento comporta l'ottimizzazione dei parametri del modello in modo che possa predire accuratamente le classi e le posizioni degli oggetti in un'immagine. L'addestramento è essenziale per creare modelli in grado di riconoscere oggetti specifici rilevanti per la tua applicazione.

Esempi di addestramento

La modalità Val viene utilizzata per validare un modello YOLO26 dopo che è stato addestrato. In questa modalità, il modello viene valutato su un set di validazione per misurarne l'accuratezza e le prestazioni di generalizzazione. La validazione aiuta a identificare potenziali problemi come l'overfitting e fornisce metriche come la mean Average Precision (mAP) per quantificare le prestazioni del modello. Questa modalità è cruciale per la messa a punto degli iperparametri e per migliorare l'efficacia complessiva del modello.

La modalità Predict viene utilizzata per effettuare predizioni utilizzando un modello YOLO26 addestrato su nuove immagini o video. In questa modalità, il modello viene caricato da un file checkpoint e l'utente può fornire immagini o video per eseguire l'inferenza. Il modello identifica e localizza gli oggetti nei media di input, rendendolo pronto per applicazioni nel mondo reale. La modalità Predict è la porta d'accesso per applicare il modello addestrato alla risoluzione di problemi pratici.

La modalità Export viene utilizzata per convertire un modello YOLO26 in formati adatti al deployment su diverse piattaforme e dispositivi. Questa modalità trasforma il tuo modello PyTorch in formati ottimizzati come ONNX, TensorRT o CoreML, consentendo il deployment in ambienti di produzione. L'esportazione è essenziale per integrare il tuo modello con varie applicazioni software o dispositivi hardware, spesso con conseguenti significativi miglioramenti delle prestazioni.

La modalità track estende le capacità di rilevamento oggetti di YOLO26 per trackare oggetti attraverso i fotogrammi video o i flussi live. Questa modalità è particolarmente preziosa per applicazioni che richiedono un'identificazione persistente degli oggetti, come i sistemi di sorveglianza o le auto a guida autonoma. La modalità track implementa algoritmi sofisticati come ByteTrack per mantenere l'identità degli oggetti tra i fotogrammi, anche quando gli oggetti scompaiono temporaneamente dalla vista.

La modalità benchmark profila la velocità e la precisione di vari formati di esportazione per YOLO26. Questa modalità fornisce metriche complete su dimensione del modello, precisione (mAP50-95 per i task di detect o accuracy_top5 per la classificazione) e tempo di inferenza attraverso diversi formati come ONNX, OpenVINO e TensorRT. Il benchmarking ti aiuta a selezionare il formato di esportazione ottimale in base ai tuoi requisiti specifici di velocità e precisione nel tuo ambiente di deployment.

L'addestramento di un modello di rilevamento oggetti personalizzato con Ultralytics YOLO26 implica l'uso della modalità di addestramento (train mode). È necessario un dataset formattato in formato YOLO, contenente immagini e i relativi file di annotazione. Utilizzare il seguente comando per avviare il processo di addestramento:

Per istruzioni più dettagliate, è possibile consultare la Guida all'addestramento di Ultralytics.

Ultralytics YOLO26 utilizza diverse metriche durante il processo di validazione per valutare le prestazioni del modello. Queste includono:

È possibile eseguire il comando seguente per avviare la convalida:

Consultare la Guida alla convalida per ulteriori dettagli.

Ultralytics YOLO26 offre funzionalità di esportazione per convertire il modello addestrato in vari formati di deployment come ONNX, TensorRT, CoreML e altri. Utilizzare il seguente esempio per esportare il modello:

I passaggi dettagliati per ogni formato di esportazione sono disponibili nella Guida all'esportazione.

La modalità benchmark in Ultralytics YOLO26 viene utilizzata per analizzare la velocità e la accuratezza di vari formati di esportazione come ONNX, TensorRT e OpenVINO. Fornisce metriche come la dimensione del modello, mAP50-95 per l'object detection e il tempo di inferenza su diverse configurazioni hardware, aiutandoti a scegliere il formato più adatto alle tue esigenze di deployment.

Per maggiori dettagli, consultare la Guida al Benchmark.

Il track di oggetti in tempo reale può essere ottenuto utilizzando la modalità track in Ultralytics YOLO26. Questa modalità estende le capacità di rilevamento oggetti per trackare oggetti attraverso i fotogrammi video o i feed live. Utilizzare il seguente esempio per abilitare il tracking:

Per istruzioni dettagliate, visitare la Guida al tracciamento.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a pretrained YOLO model (you can choose n, s, m, l, or x versions)
model = YOLO("yolo26n.pt")

# Start training on your custom dataset
model.train(data="path/to/dataset.yaml", epochs=100, imgsz=640)
```

Example 2 (sql):
```sql
# Train a YOLO model from the command line
yolo detect train data=path/to/dataset.yaml model=yolo26n.pt epochs=100 imgsz=640
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load a pretrained or custom YOLO model
model = YOLO("yolo26n.pt")

# Run validation on your dataset
model.val(data="path/to/validation.yaml")
```

Example 4 (sql):
```sql
# Validate a YOLO model from the command line
yolo val model=yolo26n.pt data=path/to/validation.yaml
```

---

## Model Benchmarking with Ultralytics YOLO

**URL:** https://docs.ultralytics.com/modes/benchmark/

**Contents:**
- Model Benchmarking with Ultralytics YOLO
- Benchmark Visualization
- Introduction
- Why Is Benchmarking Crucial?
  - Key Metrics in Benchmark Mode
  - Supported Export Formats
- Usage Examples
- Arguments
- Export Formats
- FAQ

You may need to refresh the page to view the graphs correctly due to potential cookie issues.

Once your model is trained and validated, the next logical step is to evaluate its performance in various real-world scenarios. Benchmark mode in Ultralytics YOLO26 serves this purpose by providing a robust framework for assessing the speed and accuracy of your model across a range of export formats.

Watch: Benchmark Ultralytics YOLO26 Models | How to Compare Model Performance on Different Hardware?

Run YOLO26n benchmarks across all supported export formats (ONNX, TensorRT, etc.). See the Arguments section below for a full list of export options.

Arguments such as model, data, imgsz, half, device, verbose and format provide users with the flexibility to fine-tune the benchmarks to their specific needs and compare the performance of different export formats with ease.

Benchmarks will attempt to run automatically on all possible export formats listed below. Alternatively, you can run benchmarks for a specific format by using the format argument, which accepts any of the formats mentioned below.

See full export details in the Export page.

Ultralytics YOLO26 offers a Benchmark mode to assess your model's performance across different export formats. This mode provides insights into key metrics such as mean Average Precision (mAP50-95), accuracy, and inference time in milliseconds. To run benchmarks, you can use either Python or CLI commands. For example, to benchmark on a GPU:

For more details on benchmark arguments, visit the Arguments section.

Exporting YOLO26 models to different formats such as ONNX, TensorRT, and OpenVINO allows you to optimize performance based on your deployment environment. For instance:

These formats enhance both the speed and accuracy of your models, making them more efficient for various real-world applications. Visit the Export page for complete details.

Benchmarking your YOLO26 models is essential for several reasons:

Key metrics such as mAP50-95, Top-5 accuracy, and inference time help in making these evaluations. Refer to the Key Metrics section for more information.

YOLO26 supports a variety of export formats, each tailored for specific hardware and use cases:

For a complete list of supported formats and their respective advantages, check out the Supported Export Formats section.

When running benchmarks, several arguments can be customized to suit specific needs:

For a full list of arguments, refer to the Arguments section.

**Examples:**

Example 1 (sql):
```sql
from ultralytics.utils.benchmarks import benchmark

# Benchmark on GPU
benchmark(model="yolo26n.pt", data="coco8.yaml", imgsz=640, half=False, device=0)

# Benchmark specific export format
benchmark(model="yolo26n.pt", data="coco8.yaml", imgsz=640, format="onnx")
```

Example 2 (markdown):
```markdown
yolo benchmark model=yolo26n.pt data='coco8.yaml' imgsz=640 half=False device=0

# Benchmark specific export format
yolo benchmark model=yolo26n.pt data='coco8.yaml' imgsz=640 format=onnx
```

Example 3 (sql):
```sql
from ultralytics.utils.benchmarks import benchmark

# Benchmark on GPU
benchmark(model="yolo26n.pt", data="coco8.yaml", imgsz=640, half=False, device=0)
```

Example 4 (unknown):
```unknown
yolo benchmark model=yolo26n.pt data='coco8.yaml' imgsz=640 half=False device=0
```

---

## Model Export with Ultralytics YOLO

**URL:** https://docs.ultralytics.com/modes/export/

**Contents:**
- Model Export with Ultralytics YOLO
- Introduction
- Why Choose YOLO26's Export Mode?
  - Key Features of Export Mode
- Usage Examples
- Arguments
- Export Formats
- FAQ
  - How do I export a YOLO26 model to ONNX format?
  - What are the benefits of using TensorRT for model export?

The ultimate goal of training a model is to deploy it for real-world applications. Export mode in Ultralytics YOLO26 offers a versatile range of options for exporting your trained model to different formats, making it deployable across various platforms and devices. This comprehensive guide aims to walk you through the nuances of model exporting, showcasing how to achieve maximum compatibility and performance.

Watch: How To Export Custom Trained Ultralytics YOLO Model and Run Live Inference on Webcam.

Here are some of the standout functionalities:

Export a YOLO26n model to a different format like ONNX or TensorRT. See the Arguments section below for a full list of export arguments.

This table details the configurations and options available for exporting YOLO models to different formats. These settings are critical for optimizing the exported model's performance, size, and compatibility across various platforms and environments. Proper configuration ensures that the model is ready for deployment in the intended application with optimal efficiency.

Adjusting these parameters allows for customization of the export process to fit specific requirements, such as deployment environment, hardware constraints, and performance targets. Selecting the appropriate format and settings is essential for achieving the best balance between model size, speed, and accuracy.

Available YOLO26 export formats are in the table below. You can export to any format using the format argument, i.e., format='onnx' or format='engine'. You can predict or validate directly on exported models, i.e., yolo predict model=yolo26n.onnx. Usage examples are shown for your model after export completes.

Exporting a YOLO26 model to ONNX format is straightforward with Ultralytics. It provides both Python and CLI methods for exporting models.

For more details on the process, including advanced options like handling different input sizes, refer to the ONNX integration guide.

Using TensorRT for model export offers significant performance improvements. YOLO26 models exported to TensorRT can achieve up to a 5x GPU speedup, making it ideal for real-time inference applications.

To learn more about integrating TensorRT, see the TensorRT integration guide.

INT8 quantization is an excellent way to compress the model and speed up inference, especially on edge devices. Here's how you can enable INT8 quantization:

INT8 quantization can be applied to various formats, such as TensorRT, OpenVINO, and CoreML. For optimal quantization results, provide a representative dataset using the data parameter.

Dynamic input size allows the exported model to handle varying image dimensions, providing flexibility and optimizing processing efficiency for different use cases. When exporting to formats like ONNX or TensorRT, enabling dynamic input size ensures that the model can adapt to different input shapes seamlessly.

To enable this feature, use the dynamic=True flag during export:

Dynamic input sizing is particularly useful for applications where input dimensions may vary, such as video processing or when handling images from different sources.

Understanding and configuring export arguments is crucial for optimizing model performance:

For deployment on specific hardware platforms, consider using specialized export formats like TensorRT for NVIDIA GPUs, CoreML for Apple devices, or Edge TPU for Google Coral devices.

When you export a YOLO model to formats like ONNX or TensorRT, the output tensor structure depends on the model task. Understanding these outputs is important for custom inference implementations.

For detection models (e.g., yolo26n.pt), the output is typically a single tensor shaped like (batch_size, 4 + num_classes, num_predictions) where the channels represent box coordinates plus per-class scores, and num_predictions depends on the export input resolution (and can be dynamic).

For segmentation models (e.g., yolo26n-seg.pt), you'll typically get two outputs: the first tensor shaped like (batch_size, 4 + num_classes + mask_dim, num_predictions) (boxes, class scores, and mask coefficients), and the second tensor shaped like (batch_size, mask_dim, proto_h, proto_w) containing mask prototypes used with the coefficients to generate instance masks. Sizes depend on the export input resolution (and can be dynamic).

For pose models (e.g., yolo26n-pose.pt), the output tensor is typically shaped like (batch_size, 4 + num_classes + keypoint_dims, num_predictions), where keypoint_dims depends on the pose specification (e.g., number of keypoints and whether confidence is included), and num_predictions depends on the export input resolution (and can be dynamic).

The examples in the ONNX inference examples demonstrate how to process these outputs for each model type.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load an official model
model = YOLO("path/to/best.pt")  # load a custom-trained model

# Export the model
model.export(format="onnx")
```

Example 2 (unknown):
```unknown
yolo export model=yolo26n.pt format=onnx      # export official model
yolo export model=path/to/best.pt format=onnx # export custom-trained model
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load an official model
model = YOLO("path/to/best.pt")  # load a custom-trained model

# Export the model
model.export(format="onnx")
```

Example 4 (unknown):
```unknown
yolo export model=yolo26n.pt format=onnx      # export official model
yolo export model=path/to/best.pt format=onnx # export custom-trained model
```

---

## Model Prediction with Ultralytics YOLO

**URL:** https://docs.ultralytics.com/modes/predict/

**Contents:**
- Model Prediction with Ultralytics YOLO
- Introduction
- Real-world Applications
- Why Use Ultralytics YOLO for Inference?
  - Key Features of Predict Mode
- Inference Sources
- Inference Arguments
- Image and Video Formats
  - Images
  - Videos

In the world of machine learning and computer vision, the process of making sense of visual data is often called inference or prediction. Ultralytics YOLO26 offers a powerful feature known as predict mode, tailored for high-performance, real-time inference across a wide range of data sources.

Watch: How to Extract Results from Ultralytics YOLO26 Tasks for Custom Projects 🚀

Here's why you should consider YOLO26's predict mode for your various inference needs:

YOLO26's predict mode is designed to be robust and versatile, featuring:

Ultralytics YOLO models return either a Python list of Results objects or a memory-efficient generator of Results objects when stream=True is passed to the model during inference:

YOLO26 can process different types of input sources for inference, as shown in the table below. The sources include static images, video streams, and various data formats. The table also indicates whether each source can be used in streaming mode with the argument stream=True ✅. Streaming mode is beneficial for processing videos or live streams as it creates a generator of results instead of loading all frames into memory.

Use stream=True for processing long videos or large datasets to efficiently manage memory. When stream=False, the results for all frames or data points are stored in memory, which can quickly add up and cause out-of-memory errors for large inputs. In contrast, stream=True utilizes a generator, which only keeps the results of the current frame or data point in memory, significantly reducing memory consumption and preventing out-of-memory issues.

Below are code examples for using each source type:

Run inference on an image file.

Run inference on the current screen content as a screenshot.

Run inference on an image or video hosted remotely via URL.

Run inference on an image opened with Python Imaging Library (PIL).

Run inference on an image read with OpenCV.

Run inference on an image represented as a numpy array.

Run inference on an image represented as a PyTorch tensor.

Run inference on a collection of images, URLs, videos, and directories listed in a CSV file.

Run inference on a video file. By using stream=True, you can create a generator of Results objects to reduce memory usage.

Run inference on all images and videos in a directory. To include assets in subdirectories, use a glob pattern such as path/to/dir/**/*.

Run inference on all images and videos that match a glob expression with * characters.

Run inference on a YouTube video. By using stream=True, you can create a generator of Results objects to reduce memory usage for long videos.

Use the stream mode to run inference on live video streams using RTSP, RTMP, TCP, or IP address protocols. If a single stream is provided, the model runs inference with a batch size of 1. For multiple streams, a .streams text file can be used to perform batched inference, where the batch size is determined by the number of streams provided (e.g., batch-size 8 for 8 streams).

For single stream usage, the batch size is set to 1 by default, allowing efficient real-time processing of the video feed.

To handle multiple video streams simultaneously, use a .streams text file containing one source per line. The model will run batched inference where the batch size equals the number of streams. This setup enables efficient processing of multiple feeds concurrently.

Example .streams text file:

Each row in the file represents a streaming source, allowing you to monitor and perform inference on several video streams at once.

You can run inference on a connected camera device by passing the index of that particular camera to source.

model.predict() accepts multiple arguments that can be passed at inference time to override defaults:

Ultralytics uses minimal padding during inference by default (rect=True). In this mode, the shorter side of each image is padded only as much as needed to make it divisible by the model's maximum stride, rather than padding it all the way to the full imgsz. When running inference on a batch of images, minimal padding only works if all images have identical size. Otherwise, images are uniformly padded to a square shape with both sides equal to imgsz.

Visualization arguments:

YOLO26 supports various image and video formats, as specified in ultralytics/data/utils.py. See the tables below for the valid suffixes and example predict commands.

The below table contains valid Ultralytics image formats.

HEIC images are supported for inference only, not for training.

The below table contains valid Ultralytics video formats.

All Ultralytics predict() calls will return a list of Results objects:

Results objects have the following attributes:

Results objects have the following methods:

For more details see the Results class documentation.

Boxes object can be used to index, manipulate, and convert bounding boxes to different formats.

Here is a table for the Boxes class methods and properties, including their name, type, and description:

For more details see the Boxes class documentation.

Masks object can be used index, manipulate and convert masks to segments.

Here is a table for the Masks class methods and properties, including their name, type, and description:

For more details see the Masks class documentation.

Keypoints object can be used index, manipulate and normalize coordinates.

Here is a table for the Keypoints class methods and properties, including their name, type, and description:

For more details see the Keypoints class documentation.

Probs object can be used index, get top1 and top5 indices and scores of classification.

Here's a table summarizing the methods and properties for the Probs class:

For more details see the Probs class documentation.

OBB object can be used to index, manipulate, and convert oriented bounding boxes to different formats.

Here is a table for the OBB class methods and properties, including their name, type, and description:

For more details see the OBB class documentation.

The plot() method in Results objects facilitates visualization of predictions by overlaying detected objects (such as bounding boxes, masks, keypoints, and probabilities) onto the original image. This method returns the annotated image as a NumPy array, allowing for easy display or saving.

The plot() method supports various arguments to customize the output:

Ensuring thread safety during inference is crucial when you are running multiple YOLO models in parallel across different threads. Thread-safe inference guarantees that each thread's predictions are isolated and do not interfere with one another, avoiding race conditions and ensuring consistent and reliable outputs.

When using YOLO models in a multi-threaded application, it's important to instantiate separate model objects for each thread or employ thread-local storage to prevent conflicts:

Thread-Safe Inference

Instantiate a single model inside each thread for thread-safe inference:

For an in-depth look at thread-safe inference with YOLO models and step-by-step instructions, please refer to our YOLO Thread-Safe Inference Guide. This guide will provide you with all the necessary information to avoid common pitfalls and ensure that your multi-threaded inference runs smoothly.

Here's a Python script using OpenCV (cv2) and YOLO to run inference on video frames. This script assumes you have already installed the necessary packages (opencv-python and ultralytics).

This script will run predictions on each frame of the video, visualize the results, and display them in a window. The loop can be exited by pressing 'q'.

Ultralytics YOLO is a state-of-the-art model for real-time object detection, segmentation, and classification. Its predict mode allows users to perform high-speed inference on various data sources such as images, videos, and live streams. Designed for performance and versatility, it also offers batch processing and streaming modes. For more details on its features, check out the Ultralytics YOLO predict mode.

Ultralytics YOLO can process a wide range of data sources, including individual images, videos, directories, URLs, and streams. You can specify the data source in the model.predict() call. For example, use 'image.jpg' for a local image or 'https://ultralytics.com/images/bus.jpg' for a URL. Check out the detailed examples for various inference sources in the documentation.

To optimize inference speed and manage memory efficiently, you can use the streaming mode by setting stream=True in the predictor's call method. The streaming mode generates a memory-efficient generator of Results objects instead of loading all frames into memory. For processing long videos or large datasets, streaming mode is particularly useful. Learn more about streaming mode.

The model.predict() method in YOLO supports various arguments such as conf, iou, imgsz, device, and more. These arguments allow you to customize the inference process, setting parameters like confidence thresholds, image size, and the device used for computation. Detailed descriptions of these arguments can be found in the inference arguments section.

After running inference with YOLO, the Results objects contain methods for displaying and saving annotated images. You can use methods like result.show() and result.save(filename="result.jpg") to visualize and save the results. For a comprehensive list of these methods, refer to the working with results section.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # pretrained YOLO26n model

# Run batched inference on a list of images
results = model(["image1.jpg", "image2.jpg"])  # return a list of Results objects

# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    result.show()  # display to screen
    result.save(filename="result.jpg")  # save to disk
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # pretrained YOLO26n model

# Run batched inference on a list of images
results = model(["image1.jpg", "image2.jpg"], stream=True)  # return a generator of Results objects

# Process results generator
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    result.show()  # display to screen
    result.save(filename="result.jpg")  # save to disk
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load a pretrained YOLO26n model
model = YOLO("yolo26n.pt")

# Define path to the image file
source = "path/to/image.jpg"

# Run inference on the source
results = model(source)  # list of Results objects
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a pretrained YOLO26n model
model = YOLO("yolo26n.pt")

# Define current screenshot as source
source = "screen"

# Run inference on the source
results = model(source)  # list of Results objects
```

---

## Model Training with Ultralytics YOLO

**URL:** https://docs.ultralytics.com/modes/train/

**Contents:**
- Model Training with Ultralytics YOLO
- Introduction
- Why Choose Ultralytics YOLO for Training?
  - Key Features of Train Mode
- Usage Examples
  - Multi-GPU Training
  - Idle GPU Training
  - Apple Silicon MPS Training
  - Resuming Interrupted Trainings
- Train Settings

Training a deep learning model involves feeding it data and adjusting its parameters so that it can make accurate predictions. Train mode in Ultralytics YOLO26 is engineered for effective and efficient training of object detection models, fully utilizing modern hardware capabilities. This guide aims to cover all the details you need to get started with training your own models using YOLO26's robust set of features.

Watch: How to Train a YOLO model on Your Custom Dataset in Google Colab.

Here are some compelling reasons to opt for YOLO26's Train mode:

The following are some notable features of YOLO26's Train mode:

Train YOLO26n on the COCO8 dataset for 100 epochs at image size 640. The training device can be specified using the device argument. If no argument is passed, GPU device=0 will be used when available; otherwise device='cpu' will be used. See the Arguments section below for a full list of training arguments.

Windows Multi-Processing Error

On Windows, you may receive a RuntimeError when launching the training as a script. Add an if __name__ == "__main__": block before your training code to resolve it.

Single-GPU and CPU Training Example

Device is determined automatically. If a GPU is available, it will be used (default CUDA device 0); otherwise training will start on CPU.

Multi-GPU training allows for more efficient utilization of available hardware resources by distributing the training load across multiple GPUs. This feature is available through both the Python API and the command-line interface. To enable multi-GPU training, specify the GPU device IDs you wish to use.

Multi-GPU Training Example

To train with 2 GPUs, CUDA devices 0 and 1 use the following commands. Expand to additional GPUs as required.

Idle GPU Training enables automatic selection of the least utilized GPUs in multi-GPU systems, optimizing resource usage without manual GPU selection. This feature identifies available GPUs based on utilization metrics and VRAM availability.

Idle GPU Training Example

To automatically select and use the most idle GPU(s) for training, use the -1 device parameter. This is particularly useful in shared computing environments or servers with multiple users.

The auto-selection algorithm prioritizes GPUs with:

This feature is especially valuable in shared computing environments or when running multiple training jobs across different models. It automatically adapts to changing system conditions, ensuring optimal resource allocation without manual intervention.

With the support for Apple silicon chips integrated in the Ultralytics YOLO models, it's now possible to train your models on devices utilizing the powerful Metal Performance Shaders (MPS) framework. The MPS offers a high-performance way of executing computation and image processing tasks on Apple's custom silicon.

To enable training on Apple silicon chips, you should specify 'mps' as your device when initiating the training process. Below is an example of how you could do this in Python and via the command line:

While leveraging the computational power of the Apple silicon chips, this enables more efficient processing of the training tasks. For more detailed guidance and advanced configuration options, please refer to the PyTorch MPS documentation.

Resuming training from a previously saved state is a crucial feature when working with deep learning models. This can come in handy in various scenarios, like when the training process has been unexpectedly interrupted, or when you wish to continue training a model with new data or for more epochs.

When training is resumed, Ultralytics YOLO loads the weights from the last saved model and also restores the optimizer state, learning rate scheduler, and the epoch number. This allows you to continue the training process seamlessly from where it was left off.

You can easily resume training in Ultralytics YOLO by setting the resume argument to True when calling the train method, and specifying the path to the .pt file containing the partially trained model weights.

Below is an example of how to resume an interrupted training using Python and via the command line:

Resume Training Example

By setting resume=True, the train function will continue training from where it left off, using the state stored in the 'path/to/last.pt' file. If the resume argument is omitted or set to False, the train function will start a new training session.

Remember that checkpoints are saved at the end of every epoch by default, or at fixed intervals using the save_period argument, so you must complete at least 1 epoch to resume a training run.

The training settings for YOLO models encompass various hyperparameters and configurations used during the training process. These settings influence the model's performance, speed, and accuracy. Key training settings include batch size, learning rate, momentum, and weight decay. Additionally, the choice of optimizer, loss function, and training dataset composition can impact the training process. Careful tuning and experimentation with these settings are crucial for optimizing performance.

Note on Batch-size Settings

The batch argument can be configured in three ways:

Augmentation techniques are essential for improving the robustness and performance of YOLO models by introducing variability into the training data, helping the model generalize better to unseen data. The following table outlines the purpose and effect of each augmentation argument:

These settings can be adjusted to meet the specific requirements of the dataset and task at hand. Experimenting with different values can help find the optimal augmentation strategy that leads to the best model performance.

For more information about training augmentation operations, see the reference section.

In training a YOLO26 model, you might find it valuable to keep track of the model's performance over time. This is where logging comes into play. Ultralytics YOLO provides support for three types of loggers - Comet, ClearML, and TensorBoard.

To use a logger, select it from the dropdown menu in the code snippet above and run it. The chosen logger will be installed and initialized.

Comet is a platform that allows data scientists and developers to track, compare, explain and optimize experiments and models. It provides functionalities such as real-time metrics, code diffs, and hyperparameters tracking.

Remember to sign in to your Comet account on their website and get your API key. You will need to add this to your environment variables or your script to log your experiments.

ClearML is an open-source platform that automates tracking of experiments and helps with efficient sharing of resources. It is designed to help teams manage, execute, and reproduce their ML work more efficiently.

After running this script, you will need to sign in to your ClearML account on the browser and authenticate your session.

TensorBoard is a visualization toolkit for TensorFlow. It allows you to visualize your TensorFlow graph, plot quantitative metrics about the execution of your graph, and show additional data like images that pass through it.

To use TensorBoard in Google Colab:

To use TensorBoard locally run the below command and view results at http://localhost:6006/.

This will load TensorBoard and direct it to the directory where your training logs are saved.

After setting up your logger, you can then proceed with your model training. All training metrics will be automatically logged in your chosen platform, and you can access these logs to monitor your model's performance over time, compare different models, and identify areas for improvement.

To train an object detection model using Ultralytics YOLO26, you can either use the Python API or the CLI. Below is an example for both:

Single-GPU and CPU Training Example

For more details, refer to the Train Settings section.

The key features of Ultralytics YOLO26's Train mode include:

These features make training efficient and customizable to your needs. For more details, see the Key Features of Train Mode section.

To resume training from an interrupted session, set the resume argument to True and specify the path to the last saved checkpoint.

Resume Training Example

Check the section on Resuming Interrupted Trainings for more information.

Yes, Ultralytics YOLO26 supports training on Apple silicon chips utilizing the Metal Performance Shaders (MPS) framework. Specify 'mps' as your training device.

For more details, refer to the Apple Silicon MPS Training section.

Ultralytics YOLO26 allows you to configure a variety of training settings such as batch size, learning rate, epochs, and more through arguments. Here's a brief overview:

For an in-depth guide on training settings, check the Train Settings section.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.yaml")  # build a new model from YAML
model = YOLO("yolo26n.pt")  # load a pretrained model (recommended for training)
model = YOLO("yolo26n.yaml").load("yolo26n.pt")  # build from YAML and transfer weights

# Train the model
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

Example 2 (sql):
```sql
# Build a new model from YAML and start training from scratch
yolo detect train data=coco8.yaml model=yolo26n.yaml epochs=100 imgsz=640

# Start training from a pretrained *.pt model
yolo detect train data=coco8.yaml model=yolo26n.pt epochs=100 imgsz=640

# Build a new model from YAML, transfer pretrained weights to it and start training
yolo detect train data=coco8.yaml model=yolo26n.yaml pretrained=yolo26n.pt epochs=100 imgsz=640
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load a pretrained model (recommended for training)

# Train the model with 2 GPUs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640, device=[0, 1])

# Train the model with the two most idle GPUs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640, device=[-1, -1])
```

Example 4 (julia):
```julia
# Start training from a pretrained *.pt model using GPUs 0 and 1
yolo detect train data=coco8.yaml model=yolo26n.pt epochs=100 imgsz=640 device=0,1

# Use the two most idle GPUs
yolo detect train data=coco8.yaml model=yolo26n.pt epochs=100 imgsz=640 device=-1,-1
```

---

## Model Validation with Ultralytics YOLO

**URL:** https://docs.ultralytics.com/modes/val/

**Contents:**
- Model Validation with Ultralytics YOLO
- Introduction
- Why Validate with Ultralytics YOLO?
  - Key Features of Val Mode
- Usage Examples
- Arguments for YOLO Model Validation
  - Example Validation with Arguments
- FAQ
  - How do I validate my YOLO26 model with Ultralytics?
  - What metrics can I get from YOLO26 model validation?

Validation is a critical step in the machine learning pipeline, allowing you to assess the quality of your trained models. Val mode in Ultralytics YOLO26 provides a robust suite of tools and metrics for evaluating the performance of your object detection models. This guide serves as a complete resource for understanding how to effectively use the Val mode to ensure that your models are both accurate and reliable.

Watch: Ultralytics Modes Tutorial: Validation

Here's why using YOLO26's Val mode is advantageous:

These are the notable functionalities offered by YOLO26's Val mode:

Validate a trained YOLO26n model accuracy on the COCO8 dataset. No arguments are needed as the model retains its training data and arguments as model attributes. See the Arguments section below for a full list of validation arguments.

Windows Multi-Processing Error

On Windows, you may receive a RuntimeError when launching the validation as a script. Add an if __name__ == "__main__": block before your validation code to resolve it.

When validating YOLO models, several arguments can be fine-tuned to optimize the evaluation process. These arguments control aspects such as input image size, batch processing, and performance thresholds. Below is a detailed breakdown of each argument to help you customize your validation settings effectively.

Each of these settings plays a vital role in the validation process, allowing for a customizable and efficient evaluation of YOLO models. Adjusting these parameters according to your specific needs and resources can help achieve the best balance between accuracy and performance.

Watch: How to Export Model Validation Results in CSV, JSON, SQL, Polars DataFrame & More

The below examples showcase YOLO model validation with custom arguments in Python and CLI.

Export ConfusionMatrix

You can also save the ConfusionMatrix results in different formats using the provided code.

For more details see the DataExportMixin class documentation.

To validate your YOLO26 model, you can use the Val mode provided by Ultralytics. For example, using the Python API, you can load a model and run validation with:

Alternatively, you can use the command-line interface (CLI):

For further customization, you can adjust various arguments like imgsz, batch, and conf in both Python and CLI modes. Check the Arguments for YOLO Model Validation section for the full list of parameters.

YOLO26 model validation provides several key metrics to assess model performance. These include:

Using the Python API, you can access these metrics as follows:

For a complete performance evaluation, it's crucial to review all these metrics. For more details, refer to the Key Features of Val Mode.

Using Ultralytics YOLO for validation provides several advantages:

These benefits ensure that your models are evaluated thoroughly and can be optimized for superior results. Learn more about these advantages in the Why Validate with Ultralytics YOLO section.

Yes, you can validate your YOLO26 model using a custom dataset. Specify the data argument with the path to your dataset configuration file. This file should include the path to the validation data.

Validation is performed using the model's own class names, which you can view using model.names, and which may be different to those specified in the dataset configuration file.

For more customizable options during validation, see the Example Validation with Arguments section.

To save the validation results to a JSON file, you can set the save_json argument to True when running validation. This can be done in both the Python API and CLI.

This functionality is particularly useful for further analysis or integration with other tools. Check the Arguments for YOLO Model Validation for more details.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load an official model
model = YOLO("path/to/best.pt")  # load a custom model

# Validate the model
metrics = model.val()  # no arguments needed, dataset and settings remembered
metrics.box.map  # map50-95
metrics.box.map50  # map50
metrics.box.map75  # map75
metrics.box.maps  # a list containing mAP50-95 for each category
```

Example 2 (unknown):
```unknown
yolo detect val model=yolo26n.pt      # val official model
yolo detect val model=path/to/best.pt # val custom model
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")

# Customize validation settings
metrics = model.val(data="coco8.yaml", imgsz=640, batch=16, conf=0.25, iou=0.7, device="0")
```

Example 4 (unknown):
```unknown
yolo val model=yolo26n.pt data=coco8.yaml imgsz=640 batch=16 conf=0.25 iou=0.7 device=0
```

---

## Multi-Object Tracking with Ultralytics YOLO

**URL:** https://docs.ultralytics.com/modes/track/

**Contents:**
- Multi-Object Tracking with Ultralytics YOLO
- Why Choose Ultralytics YOLO for Object Tracking?
- Real-world Applications
- Features at a Glance
- Available Trackers
- Tracking
- Configuration
  - Tracking Arguments
  - Tracker Selection
  - Tracker Arguments

Object tracking in the realm of video analytics is a critical task that not only identifies the location and class of objects within the frame but also maintains a unique ID for each detected object as the video progresses. The applications are limitless—ranging from surveillance and security to real-time sports analytics.

The output from Ultralytics trackers is consistent with standard object detection but has the added value of object IDs. This makes it easy to track objects in video streams and perform subsequent analytics. Here's why you should consider using Ultralytics YOLO for your object tracking needs:

Watch: Object Detection and Tracking with Ultralytics YOLO.

Ultralytics YOLO extends its object detection features to provide robust and versatile object tracking:

Ultralytics YOLO supports the following tracking algorithms. They can be enabled by passing the relevant YAML configuration file such as tracker=tracker_type.yaml:

The default tracker is BoT-SORT.

To run the tracker on video streams, use a trained Detect, Segment, or Pose model such as YOLO26n, YOLO26n-seg, or YOLO26n-pose.

As can be seen in the above usage, tracking is available for all Detect, Segment, and Pose models run on videos or streaming sources.

Tracking configuration shares properties with Predict mode, such as conf, iou, and show. For further configurations, refer to the Predict model page.

Ultralytics also allows you to use a modified tracker configuration file. To do this, simply make a copy of a tracker config file (for example, custom_tracker.yaml) from ultralytics/cfg/trackers and modify any configurations (except the tracker_type) as per your needs.

Refer to Tracker Arguments section for a detailed description of each parameter.

Some tracking behaviors can be fine-tuned by editing the YAML configuration files specific to each tracking algorithm. These files define parameters like thresholds, buffers, and matching logic:

The following table provides a description of each parameter:

Tracker Threshold Information

If a detection's confidence score falls below track_high_thresh, the tracker will not update that object, resulting in no active tracks.

By default, ReID is turned off to minimize performance overhead. Enabling it is simple—just set with_reid: True in the tracker configuration. You can also customize the model used for ReID, allowing you to trade off accuracy and speed depending on your use case:

For better performance, especially when using a separate classification model for ReID, you can export it to a faster backend like TensorRT:

Exporting a ReID model to TensorRT

Once exported, you can point to the TensorRT model path in your tracker config, and it will be used for ReID during tracking.

Watch: How to Build Interactive Object Tracking with Ultralytics YOLO | Click to Crop & Display ⚡

Here is a Python script using OpenCV (cv2) and YOLO26 to run object tracking on video frames. This script assumes the necessary packages (opencv-python and ultralytics) are already installed. The persist=True argument tells the tracker that the current image or frame is the next in a sequence and to expect tracks from the previous image in the current image.

Streaming for-loop with tracking

Please note the change from model(frame) to model.track(frame), which enables object tracking instead of simple detection. This modified script will run the tracker on each frame of the video, visualize the results, and display them in a window. The loop can be exited by pressing 'q'.

Visualizing object tracks over consecutive frames can provide valuable insights into the movement patterns and behavior of detected objects within a video. With Ultralytics YOLO26, plotting these tracks is a seamless and efficient process.

In the following example, we demonstrate how to utilize YOLO26's tracking capabilities to plot the movement of detected objects across multiple video frames. This script involves opening a video file, reading it frame by frame, and utilizing the YOLO model to identify and track various objects. By retaining the center points of the detected bounding boxes and connecting them, we can draw lines that represent the paths followed by the tracked objects.

Plotting tracks over multiple video frames

Multithreaded tracking provides the capability to run object tracking on multiple video streams simultaneously. This is particularly useful when handling multiple video inputs, such as from multiple surveillance cameras, where concurrent processing can greatly enhance efficiency and performance.

In the provided Python script, we make use of Python's threading module to run multiple instances of the tracker concurrently. Each thread is responsible for running the tracker on one video file, and all the threads run simultaneously in the background.

To ensure that each thread receives the correct parameters (the video file, the model to use and the file index), we define a function run_tracker_in_thread that accepts these parameters and contains the main tracking loop. This function reads the video frame by frame, runs the tracker, and displays the results.

Two different models are used in this example: yolo26n.pt and yolo26n-seg.pt, each tracking objects in a different video file. The video files are specified in SOURCES.

The daemon=True parameter in threading.Thread means that these threads will be closed as soon as the main program finishes. We then start the threads with start() and use join() to make the main thread wait until both tracker threads have finished.

Finally, after all threads have completed their task, the windows displaying the results are closed using cv2.destroyAllWindows().

Multithreaded tracking implementation

This example can easily be extended to handle more video files and models by creating more threads and applying the same methodology.

Are you proficient in multi-object tracking and have successfully implemented or adapted a tracking algorithm with Ultralytics YOLO? We invite you to contribute to our Trackers section in ultralytics/cfg/trackers! Your real-world applications and solutions could be invaluable for users working on tracking tasks.

By contributing to this section, you help expand the scope of tracking solutions available within the Ultralytics YOLO framework, adding another layer of functionality and utility for the community.

To initiate your contribution, please refer to our Contributing Guide for comprehensive instructions on submitting a Pull Request (PR) 🛠️. We are excited to see what you bring to the table!

Together, let's enhance the tracking capabilities of the Ultralytics YOLO ecosystem 🙏!

Multi-object tracking in video analytics involves both identifying objects and maintaining a unique ID for each detected object across video frames. Ultralytics YOLO supports this by providing real-time tracking along with object IDs, facilitating tasks such as security surveillance and sports analytics. The system uses trackers like BoT-SORT and ByteTrack, which can be configured via YAML files.

You can configure a custom tracker by copying an existing tracker configuration file (e.g., custom_tracker.yaml) from the Ultralytics tracker configuration directory and modifying parameters as needed, except for the tracker_type. Use this file in your tracking model like so:

To run object tracking on multiple video streams simultaneously, you can use Python's threading module. Each thread will handle a separate video stream. Here's an example of how you can set this up:

Multithreaded Tracking

Multi-object tracking with Ultralytics YOLO has numerous applications, including:

These applications benefit from Ultralytics YOLO's ability to process high-frame-rate videos in real time with exceptional accuracy.

To visualize object tracks over multiple video frames, you can use the YOLO model's tracking features along with OpenCV to draw the paths of detected objects. Here's an example script that demonstrates this:

Plotting tracks over multiple video frames

This script will plot the tracking lines showing the movement paths of the tracked objects over time, providing valuable insights into object behavior and patterns.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load an official or custom model
model = YOLO("yolo26n.pt")  # Load an official Detect model
model = YOLO("yolo26n-seg.pt")  # Load an official Segment model
model = YOLO("yolo26n-pose.pt")  # Load an official Pose model
model = YOLO("path/to/best.pt")  # Load a custom-trained model

# Perform tracking with the model
results = model.track("https://youtu.be/LNwODJXcvt4", show=True)  # Tracking with default tracker
results = model.track("https://youtu.be/LNwODJXcvt4", show=True, tracker="bytetrack.yaml")  # with ByteTrack
```

Example 2 (julia):
```julia
# Perform tracking with various models using the command line interface
yolo track model=yolo26n.pt source="https://youtu.be/LNwODJXcvt4"      # Official Detect model
yolo track model=yolo26n-seg.pt source="https://youtu.be/LNwODJXcvt4"  # Official Segment model
yolo track model=yolo26n-pose.pt source="https://youtu.be/LNwODJXcvt4" # Official Pose model
yolo track model=path/to/best.pt source="https://youtu.be/LNwODJXcvt4" # Custom trained model

# Track using ByteTrack tracker
yolo track model=path/to/best.pt source="https://youtu.be/LNwODJXcvt4" tracker="bytetrack.yaml"
```

Example 3 (python):
```python
from ultralytics import YOLO

# Configure the tracking parameters and run the tracker
model = YOLO("yolo26n.pt")
results = model.track(source="https://youtu.be/LNwODJXcvt4", conf=0.1, iou=0.7, show=True)
```

Example 4 (julia):
```julia
# Configure tracking parameters and run the tracker using the command line interface
yolo track model=yolo26n.pt source="https://youtu.be/LNwODJXcvt4" conf=0.1 iou=0.7 show
```

---

## Oriented Bounding Box Object Detection

**URL:** https://docs.ultralytics.com/it/tasks/obb/

**Contents:**
- Oriented Bounding Box Object Detection
- Esempi visivi
- Modelli
- Addestramento
  - Formato del set di dati
- Valutazione
- Predizione
- Esportazione
- Applicazioni nel mondo reale
- FAQ

Il rilevamento di oggetti orientati va un passo oltre il rilevamento di oggetti standard, introducendo un angolo aggiuntivo per localizzare gli oggetti in modo più preciso in un'immagine.

L'output di un rilevatore di oggetti orientati è un insieme di bounding box ruotati che racchiudono precisamente gli oggetti nell'immagine, insieme alle etichette di classe e ai punteggi di confidenza per ogni box. I bounding box orientati sono particolarmente utili quando gli oggetti appaiono a varie angolazioni, come nelle immagini aeree, dove i tradizionali bounding box allineati agli assi possono includere uno sfondo non necessario.

I modelli YOLO26 obb utilizzano il -obb suffisso, ad esempio, yolo26n-obb.pt, e sono pre-addestrati su DOTAv1.

Guarda: Rilevamento di oggetti utilizzando Ultralytics YOLO Oriented Bounding Boxes (YOLO-OBB)

Qui sono mostrati i modelli obb pre-addestrati di YOLO26, che sono stati pre-addestrati sul dataset DOTAv1.

I modelli vengono scaricati automaticamente dall'ultima release di Ultralytics al primo utilizzo.

Addestra YOLO26n-obb sul dataset DOTA8 per 100 epoche con dimensione immagine 640. Per un elenco completo degli argomenti disponibili, consulta la pagina Configurazione.

Gli angoli OBB sono vincolati all'intervallo 0–90 gradi (90 escluso). Gli angoli di 90 gradi o superiori non sono supportati.

Guarda: Come addestrare modelli Ultralytics YOLO-OBB (Bounding Box Orientate) sul dataset DOTA utilizzando la piattaforma Ultralytics

Il formato del dataset OBB può essere trovato in dettaglio nella Guida al Dataset. Il formato YOLO OBB designa i riquadri di delimitazione tramite i loro quattro punti d'angolo con coordinate normalizzate tra 0 e 1, seguendo questa struttura:

Internamente, YOLO elabora le perdite e gli output in xywhr formato, che rappresenta il riquadro di delimitazioneil punto centrale (xy), la larghezza, l'altezza e la rotazione di .

Validare il modello YOLO26n-obb addestrato accuratezza sul dataset DOTA8. Non sono necessari argomenti poiché il model mantiene il suo training data e gli argomenti come attributi del modello.

Utilizzare un modello YOLO26n-obb addestrato per eseguire previsioni su immagini.

Guarda: Come rilevare e tracciare serbatoi di stoccaggio utilizzando Ultralytics YOLO-OBB | Bounding box orientati | DOTA

Vedi tutti i predict dettagli della modalità nella Predizione pagina.

Esportare un modello YOLO26n-obb in un formato diverso come ONNX, CoreML, ecc.

I formati di esportazione YOLO26-obb disponibili sono nella tabella seguente. È possibile esportare in qualsiasi formato utilizzando il format argomento, cioè, format='onnx' oppure format='engine'. È possibile effettuare previsioni o validazioni direttamente sui modelli esportati, cioè, yolo predict model=yolo26n-obb.onnx. Esempi di utilizzo vengono mostrati per il tuo modello dopo che l'esportazione è stata completata.

Vedi tutti i export dettagli nella Esportazione pagina.

La OBB detection con YOLO26 ha numerose applicazioni pratiche in diversi settori industriali:

Queste applicazioni traggono vantaggio dalla capacità di OBB di adattare con precisione gli oggetti a qualsiasi angolazione, fornendo una detection più accurata rispetto alle tradizionali bounding box.

Gli Oriented Bounding Box (OBB) includono un angolo aggiuntivo per migliorare l'accuratezza della localizzazione degli oggetti nelle immagini. A differenza delle normali bounding box, che sono rettangoli allineati agli assi, gli OBB possono ruotare per adattarsi meglio all'orientamento dell'oggetto. Questo è particolarmente utile per le applicazioni che richiedono un posizionamento preciso degli oggetti, come le immagini aeree o satellitari (Guida al set di dati).

Per addestrare un modello YOLO26n-obb con un dataset personalizzato, seguire l'esempio seguente utilizzando Python o CLI:

Per ulteriori argomenti di training, consultare la sezione Configurazione.

I modelli YOLO26-OBB sono pre-addestrati su dataset come DOTAv1 ma è possibile utilizzare qualsiasi dataset formattato per OBB. Informazioni dettagliate sui formati dei dataset OBB sono disponibili nella Guida ai Dataset.

Esportare un modello YOLO26-OBB nel formato ONNX è semplice utilizzando Python o CLI:

Per ulteriori formati di esportazione e dettagli, consulta la pagina Esportazione.

Per validare un modello YOLO26n-obb, è possibile utilizzare i comandi Python o CLI come mostrato di seguito:

Vedi i dettagli completi della convalida nella sezione Val.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-obb.yaml")  # build a new model from YAML
model = YOLO("yolo26n-obb.pt")  # load a pretrained model (recommended for training)
model = YOLO("yolo26n-obb.yaml").load("yolo26n.pt")  # build from YAML and transfer weights

# Train the model
results = model.train(data="dota8.yaml", epochs=100, imgsz=640)
```

Example 2 (sql):
```sql
# Build a new model from YAML and start training from scratch
yolo obb train data=dota8.yaml model=yolo26n-obb.yaml epochs=100 imgsz=640

# Start training from a pretrained *.pt model
yolo obb train data=dota8.yaml model=yolo26n-obb.pt epochs=100 imgsz=640

# Build a new model from YAML, transfer pretrained weights to it and start training
yolo obb train data=dota8.yaml model=yolo26n-obb.yaml pretrained=yolo26n-obb.pt epochs=100 imgsz=640
```

Example 3 (unknown):
```unknown
class_index x1 y1 x2 y2 x3 y3 x4 y4
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-obb.pt")  # load an official model
model = YOLO("path/to/best.pt")  # load a custom model

# Validate the model
metrics = model.val(data="dota8.yaml")  # no arguments needed, dataset and settings remembered
metrics.box.map  # map50-95(B)
metrics.box.map50  # map50(B)
metrics.box.map75  # map75(B)
metrics.box.maps  # a list containing mAP50-95(B) for each category
```

---

## Predizione del modello con Ultralytics YOLO

**URL:** https://docs.ultralytics.com/it/modes/predict/

**Contents:**
- Predizione del modello con Ultralytics YOLO
- Introduzione
- Applicazioni nel mondo reale
- Perché utilizzare Ultralytics YOLO per l'inferenza?
  - Caratteristiche principali della modalità Predict
- Sorgenti di inferenza
- Argomenti di inferenza
- Formati di immagine e video
  - Immagini
  - Video

Nel mondo del machine learning e della computer vision, il processo di interpretazione dei dati visivi è spesso chiamato inferenza o previsione. Ultralytics YOLO26 offre una potente funzionalità nota come modalità di previsione, progettata per l'inferenza ad alte prestazioni e in tempo reale su un'ampia gamma di fonti di dati.

Guarda: Come estrarre i risultati dalle attività Ultralytics YOLO26 per progetti personalizzati 🚀

Ecco perché dovresti considerare la modalità di previsione di YOLO26 per le tue diverse esigenze di inferenza:

La modalità di previsione di YOLO26 è progettata per essere robusta e versatile, e presenta:

I modelli Ultralytics YOLO restituiscono un elenco Python di Results objects o un generatore di memoria efficiente di Results oggetti efficiente in termini di memoria quando stream=True viene passato al modello durante l'inferenza:

YOLO26 può elaborare diversi tipi di sorgenti di input per l'inferenza, come mostrato nella tabella seguente. Le sorgenti includono immagini statiche, flussi video e vari formati di dati. La tabella indica anche se ciascuna sorgente può essere utilizzata in modalità streaming con l'argomento stream=True ✅. La modalità streaming è utile per l'elaborazione di video o flussi live in quanto crea un generatore di risultati invece di caricare tutti i fotogrammi in memoria.

Usa stream=True per l'elaborazione di video lunghi o set di dati di grandi dimensioni per gestire efficientemente la memoria. Quando stream=False, i risultati per tutti i frame o punti dati vengono memorizzati in memoria, il che può sommarsi rapidamente e causare errori di memoria insufficiente per input di grandi dimensioni. Al contrario, stream=True utilizza un generatore, che mantiene in memoria solo i risultati del frame o del punto dati corrente, riducendo significativamente il consumo di memoria e prevenendo problemi di memoria insufficiente.

Di seguito sono riportati esempi di codice per l'utilizzo di ciascun tipo di sorgente:

Sorgenti di previsione

Esegui l'inferenza su un file immagine.

Esegui l'inferenza sul contenuto corrente dello schermo come screenshot.

Esegui l'inferenza su un'immagine o un video ospitato da remoto tramite URL.

Esegui l'inferenza su un'immagine aperta con Python Imaging Library (PIL).

Esegui l'inferenza su un'immagine letta con OpenCV.

Esegui l'inferenza su un'immagine rappresentata come un array numpy.

Esegui l'inferenza su un'immagine rappresentata come un tensor PyTorch.

Esegui l'inferenza su una raccolta di immagini, URL, video e directory elencati in un file CSV.

Esegui l'inferenza su un file video. Utilizzando stream=True, puoi creare un generatore di oggetti Results per ridurre l'utilizzo della memoria.

Esegui l'inferenza su tutte le immagini e i video in una directory. Per includere risorse nelle sottodirectory, usa un modello glob come path/to/dir/**/*.

Esegui l'inferenza su tutte le immagini e i video che corrispondono a un'espressione glob con * caratteri.

Esegui l'inferenza su un video di YouTube. Utilizzando stream=True, puoi creare un generatore di oggetti Results per ridurre l'utilizzo della memoria per i video lunghi.

Utilizza la modalità stream per eseguire l'inferenza su flussi video live utilizzando i protocolli RTSP, RTMP, TCP o indirizzo IP. Se viene fornito un singolo flusso, il modello esegue l'inferenza con una dimensione del batch pari a 1. Per più flussi, è possibile utilizzare un .streams file di testo per eseguire l'inferenza in batch, dove la dimensione del batch è determinata dal numero di flussi forniti (ad esempio, dimensione del batch 8 per 8 flussi).

Per l'utilizzo di un singolo flusso, la dimensione del batch è impostata su 1 per impostazione predefinita, consentendo un'elaborazione efficiente in tempo reale del feed video.

Per gestire più flussi video contemporaneamente, utilizza un .streams file di testo contenente una sorgente per riga. Il modello eseguirà l'inferenza in batch dove la dimensione del batch è uguale al numero di stream. Questa configurazione consente l'elaborazione efficiente di più feed contemporaneamente.

Esempio .streams file di testo:

Ogni riga nel file rappresenta una sorgente di streaming, consentendoti di monitorare ed eseguire l'inferenza su diversi flussi video contemporaneamente.

Puoi eseguire l'inferenza su un dispositivo fotocamera collegato passando l'indice di quella particolare fotocamera a source.

model.predict() accetta più argomenti che possono essere passati al momento dell'inferenza per sovrascrivere i valori predefiniti:

Ultralytics utilizza un padding minimo durante l'inferenza per impostazione predefinita (rect=True). In questa modalità, il lato più corto di ogni immagine viene riempito solo quanto necessario per renderlo divisibile per il passo massimo del modello, piuttosto che riempirlo completamente fino al imgsz. Quando si esegue l'inferenza su un batch di immagini, il padding minimo funziona solo se tutte le immagini hanno le stesse dimensioni. Altrimenti, le immagini vengono uniformemente sottoposte a padding in una forma quadrata con entrambi i lati uguali a imgsz.

Argomenti di inferenza:

Argomenti di visualizzazione:

YOLO26 supporta vari formati di immagine e video, come specificato in ultralytics/data/utils.py. Vedi le tabelle seguenti per i suffissi validi e i comandi di previsione di esempio.

La tabella seguente contiene i formati immagine Ultralytics validi.

Le immagini HEIC sono supportate solo per l'inferenza, non per l'addestramento.

La tabella seguente contiene i formati video Ultralytics validi.

Tutte le chiamate Ultralytics predict() restituiranno un elenco di Results oggetti:

Results gli oggetti hanno i seguenti attributi:

Results Gli oggetti hanno i seguenti metodi:

Per maggiori dettagli, consultare la Results documentazione della classe.

Boxes L'oggetto può essere utilizzato per indicizzare, manipolare e convertire i riquadri di delimitazione in diversi formati.

Ecco una tabella per i Boxes metodi e le proprietà della classe, inclusi il nome, il tipo e la descrizione:

Per maggiori dettagli, consultare la Boxes documentazione della classe.

Masks L'oggetto può essere utilizzato per indicizzare, manipolare e convertire le maschere in segmenti.

Ecco una tabella per i Masks metodi e le proprietà della classe, inclusi il nome, il tipo e la descrizione:

Per maggiori dettagli, consultare la Masks documentazione della classe.

Keypoints L'oggetto può essere utilizzato per indicizzare, manipolare e normalizzare le coordinate.

Ecco una tabella per i Keypoints metodi e le proprietà della classe, inclusi il nome, il tipo e la descrizione:

Per maggiori dettagli, consultare la Keypoints documentazione della classe.

Probs L'oggetto può essere utilizzato per indicizzare, ottenere top1 e top5 indici e punteggi della classificazione.

Ecco una tabella che riassume i metodi e le proprietà per la Probs classe:

Per maggiori dettagli, consultare la Probs documentazione della classe.

OBB L'oggetto può essere utilizzato per indicizzare, manipolare e convertire i bounding box orientati in diversi formati.

Ecco una tabella per i OBB metodi e le proprietà della classe, inclusi il nome, il tipo e la descrizione:

Per maggiori dettagli, consultare la OBB documentazione della classe.

Il plot() metodo in Results objects facilita la visualizzazione delle previsioni sovrapponendo gli oggetti rilevati (come bounding box, maschere, punti chiave e probabilità) sull'immagine originale. Questo metodo restituisce l'immagine annotata come un array NumPy, consentendo una facile visualizzazione o salvataggio.

Il plot() Il metodo supporta vari argomenti per personalizzare l'output:

Garantire la thread safety durante l'inferenza è fondamentale quando si eseguono più modelli YOLO in parallelo su diversi thread. L'inferenza thread-safe garantisce che le predizioni di ciascun thread siano isolate e non interferiscano tra loro, evitando race condition e garantendo output coerenti e affidabili.

Quando si utilizzano modelli YOLO in un'applicazione multi-thread, è importante istanziare oggetti modello separati per ciascun thread o impiegare lo storage thread-local per prevenire conflitti:

Inferenza thread-safe

Istanza un singolo modello all'interno di ciascun thread per un'inferenza thread-safe:

Per un'analisi approfondita dell'inferenza thread-safe con i modelli YOLO e istruzioni dettagliate, consulta la nostra Guida all'inferenza thread-safe di YOLO. Questa guida ti fornirà tutte le informazioni necessarie per evitare insidie comuni e garantire che la tua inferenza multi-thread funzioni senza problemi.

Ecco uno script Python che utilizza OpenCV (cv2) e YOLO per eseguire l'inferenza sui frame video. Questo script presuppone che tu abbia già installato i pacchetti necessari (opencv-python e ultralytics).

Questo script eseguirà predizioni su ciascun frame del video, visualizzerà i risultati e li mostrerà in una finestra. È possibile uscire dal loop premendo 'q'.

Ultralytics YOLO è un modello all'avanguardia per il rilevamento di oggetti, la segmentazione e la classificazione in tempo reale. La sua modalità predict consente agli utenti di eseguire inferenze ad alta velocità su varie sorgenti di dati come immagini, video e streaming live. Progettato per prestazioni e versatilità, offre anche modalità di elaborazione batch e streaming. Per maggiori dettagli sulle sue funzionalità, consulta la modalità predict di Ultralytics YOLO.

Ultralytics YOLO è in grado di elaborare un'ampia gamma di sorgenti dati, tra cui singole immagini, video, directory, URL e stream. È possibile specificare la sorgente dati nel model.predict() comando. Ad esempio, utilizzare 'image.jpg' per un'immagine locale o 'https://ultralytics.com/images/bus.jpg' per un URL. Consultare gli esempi dettagliati per le varie sorgenti di inferenza nella documentazione.

Per ottimizzare la velocità di inferenza e gestire la memoria in modo efficiente, è possibile utilizzare la modalità streaming impostando stream=True nel metodo call del predittore. La modalità streaming genera un generatore di oggetti a basso consumo di memoria Results invece di caricare tutti i frame in memoria. Per l'elaborazione di video lunghi o set di dati di grandi dimensioni, la modalità streaming è particolarmente utile. Ulteriori informazioni sul modalità streaming.

Il model.predict() il metodo in YOLO supporta vari argomenti come conf, iou, imgsz, devicee altro ancora. Questi argomenti consentono di personalizzare il processo di inferenza, impostando parametri come le soglie di confidenza, le dimensioni dell'immagine e il dispositivo utilizzato per il calcolo. Descrizioni dettagliate di questi argomenti sono disponibili nella sezione argomenti di inferenza sezione.

Dopo aver eseguito l'inferenza con YOLO, gli Results oggetti contengono metodi per visualizzare e salvare le immagini annotate. È possibile utilizzare metodi come result.show() e result.save(filename="result.jpg") per visualizzare e salvare i risultati. Per un elenco completo di questi metodi, consultare la sezione lavorare con i risultati sezione.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # pretrained YOLO26n model

# Run batched inference on a list of images
results = model(["image1.jpg", "image2.jpg"])  # return a list of Results objects

# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    result.show()  # display to screen
    result.save(filename="result.jpg")  # save to disk
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # pretrained YOLO26n model

# Run batched inference on a list of images
results = model(["image1.jpg", "image2.jpg"], stream=True)  # return a generator of Results objects

# Process results generator
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    result.show()  # display to screen
    result.save(filename="result.jpg")  # save to disk
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load a pretrained YOLO26n model
model = YOLO("yolo26n.pt")

# Define path to the image file
source = "path/to/image.jpg"

# Run inference on the source
results = model(source)  # list of Results objects
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a pretrained YOLO26n model
model = YOLO("yolo26n.pt")

# Define current screenshot as source
source = "screen"

# Run inference on the source
results = model(source)  # list of Results objects
```

---

## Quick Start Guide: NVIDIA Jetson with Ultralytics YOLO26

**URL:** https://docs.ultralytics.com/guides/nvidia-jetson/

**Contents:**
- Quick Start Guide: NVIDIA Jetson with Ultralytics YOLO26
- What is NVIDIA Jetson?
- NVIDIA Jetson Series Comparison
- What is NVIDIA JetPack?
- Flash JetPack to NVIDIA Jetson
- JetPack Support Based on Jetson Device
- Quick Start with Docker
- Start with Native Installation
  - Run on JetPack 7.0
    - Install Ultralytics Package

This comprehensive guide provides a detailed walkthrough for deploying Ultralytics YOLO26 on NVIDIA Jetson devices. Additionally, it showcases performance benchmarks to demonstrate the capabilities of YOLO26 on these small and powerful devices.

We have updated this guide with the latest NVIDIA Jetson AGX Thor Developer Kit which delivers up to 2070 FP4 TFLOPS of AI compute and 128 GB of memory with power configurable between 40 W and 130 W. It delivers over 7.5x higher AI compute than NVIDIA Jetson AGX Orin, with 3.5x better energy efficiency to seamlessly run the most popular AI models.

Watch: How to use Ultralytics YOLO26 on NVIDIA Jetson Devices

This guide has been tested with NVIDIA Jetson AGX Thor Developer Kit (Jetson T5000) running the latest stable JetPack release of JP7.0, NVIDIA Jetson AGX Orin Developer Kit (64GB) running JetPack release of JP6.2, NVIDIA Jetson Orin Nano Super Developer Kit running JetPack release of JP6.1, Seeed Studio reComputer J4012 which is based on NVIDIA Jetson Orin NX 16GB running JetPack release of JP6.0/ JetPack release of JP5.1.3 and Seeed Studio reComputer J1020 v2 which is based on NVIDIA Jetson Nano 4GB running JetPack release of JP4.6.1. It is expected to work across all the NVIDIA Jetson hardware lineup, including the latest and legacy devices.

NVIDIA Jetson is a series of embedded computing boards designed to bring accelerated AI (artificial intelligence) computing to edge devices. These compact and powerful devices are built around NVIDIA's GPU architecture and can run complex AI algorithms and deep learning models directly on the device, without relying on cloud computing resources. Jetson boards are often used in robotics, autonomous vehicles, industrial automation, and other applications where AI inference needs to be performed locally with low latency and high efficiency. Additionally, these boards are based on the ARM64 architecture and run at lower power compared to traditional GPU computing devices.

NVIDIA Jetson AGX Thor is the latest iteration of the NVIDIA Jetson family based on NVIDIA Blackwell architecture which brings drastically improved AI performance when compared to the previous generations. The table below compares a few of the Jetson devices in the ecosystem.

For a more detailed comparison table, please visit the Compare Specifications section of official NVIDIA Jetson page.

NVIDIA JetPack SDK powering the Jetson modules is the most comprehensive solution and provides full development environment for building end-to-end accelerated AI applications and shortens time to market. JetPack includes Jetson Linux with bootloader, Linux kernel, Ubuntu desktop environment, and a complete set of libraries for acceleration of GPU computing, multimedia, graphics, and computer vision. It also includes samples, documentation, and developer tools for both host computer and developer kit, and supports higher level SDKs such as DeepStream for streaming video analytics, Isaac for robotics, and Riva for conversational AI.

The first step after getting your hands on an NVIDIA Jetson device is to flash NVIDIA JetPack to the device. There are several different ways of flashing NVIDIA Jetson devices.

For methods 1, 4 and 5 above, after flashing the system and booting the device, please enter "sudo apt update && sudo apt install nvidia-jetpack -y" on the device terminal to install all the remaining JetPack components needed.

The below table highlights NVIDIA JetPack versions supported by different NVIDIA Jetson devices.

The fastest way to get started with Ultralytics YOLO26 on NVIDIA Jetson is to run with pre-built docker images for Jetson. Refer to the table above and choose the JetPack version according to the Jetson device you own.

After this is done, skip to Use TensorRT on NVIDIA Jetson section.

For a native installation without Docker, please refer to the steps below.

Here we will install Ultralytics package on the Jetson with optional dependencies so that we can export the PyTorch models to other different formats. We will mainly focus on NVIDIA TensorRT exports because TensorRT will make sure we can get the maximum performance out of the Jetson devices.

Update packages list, install pip and upgrade to latest

Install ultralytics pip package with optional dependencies

The above ultralytics installation will install Torch and Torchvision. However, these 2 packages installed via pip are not compatible to run on Jetson AGX Thor which comes with JetPack 7.0 and CUDA 13. Therefore, we need to manually install them.

Install torch and torchvision according to JP7.0

The onnxruntime-gpu package hosted in PyPI does not have aarch64 binaries for the Jetson. So we need to manually install this package. This package is needed for some of the exports.

Here we will download and install onnxruntime-gpu 1.24.0 with Python3.12 support.

Here we will install Ultralytics package on the Jetson with optional dependencies so that we can export the PyTorch models to other different formats. We will mainly focus on NVIDIA TensorRT exports because TensorRT will make sure we can get the maximum performance out of the Jetson devices.

Update packages list, install pip and upgrade to latest

Install ultralytics pip package with optional dependencies

The above ultralytics installation will install Torch and Torchvision. However, these two packages installed via pip are not compatible with the Jetson platform, which is based on ARM64 architecture. Therefore, we need to manually install a pre-built PyTorch pip wheel and compile or install Torchvision from source.

Install torch 2.5.0 and torchvision 0.20 according to JP6.1

Visit the PyTorch for Jetson page to access all different versions of PyTorch for different JetPack versions. For a more detailed list on the PyTorch, Torchvision compatibility, visit the PyTorch and Torchvision compatibility page.

Install cuSPARSELt to fix a dependency issue with torch 2.5.0

The onnxruntime-gpu package hosted in PyPI does not have aarch64 binaries for the Jetson. So we need to manually install this package. This package is needed for some of the exports.

You can find all available onnxruntime-gpu packages—organized by JetPack version, Python version, and other compatibility details—in the Jetson Zoo ONNX Runtime compatibility matrix.

For JetPack 6 with Python 3.10 support, you can install onnxruntime-gpu 1.23.0:

Alternatively, for onnxruntime-gpu 1.20.0:

Here we will install Ultralytics package on the Jetson with optional dependencies so that we can export the PyTorch models to other different formats. We will mainly focus on NVIDIA TensorRT exports because TensorRT will make sure we can get the maximum performance out of the Jetson devices.

Update packages list, install pip and upgrade to latest

Install ultralytics pip package with optional dependencies

The above ultralytics installation will install Torch and Torchvision. However, these two packages installed via pip are not compatible with the Jetson platform, which is based on ARM64 architecture. Therefore, we need to manually install a pre-built PyTorch pip wheel and compile or install Torchvision from source.

Uninstall currently installed PyTorch and Torchvision

Install torch 2.2.0 and torchvision 0.17.2 according to JP5.1.2

Visit the PyTorch for Jetson page to access all different versions of PyTorch for different JetPack versions. For a more detailed list on the PyTorch, Torchvision compatibility, visit the PyTorch and Torchvision compatibility page.

The onnxruntime-gpu package hosted in PyPI does not have aarch64 binaries for the Jetson. So we need to manually install this package. This package is needed for some of the exports.

You can find all available onnxruntime-gpu packages—organized by JetPack version, Python version, and other compatibility details—in the Jetson Zoo ONNX Runtime compatibility matrix. Here we will download and install onnxruntime-gpu 1.17.0 with Python3.8 support.

onnxruntime-gpu will automatically revert back the numpy version to latest. So we need to reinstall numpy to 1.23.5 to fix an issue by executing:

pip install numpy==1.23.5

Among all the model export formats supported by Ultralytics, TensorRT offers the highest inference performance on NVIDIA Jetson devices, making it our top recommendation for Jetson deployments. For setup instructions and advanced usage, see our dedicated TensorRT integration guide.

The YOLO26n model in PyTorch format is converted to TensorRT to run inference with the exported model.

Visit the Export page to access additional arguments when exporting models to different model formats

NVIDIA Deep Learning Accelerator (DLA) is a specialized hardware component built into NVIDIA Jetson devices that optimizes deep learning inference for energy efficiency and performance. By offloading tasks from the GPU (freeing it up for more intensive processes), DLA enables models to run with lower power consumption while maintaining high throughput, ideal for embedded systems and real-time AI applications.

The following Jetson devices are equipped with DLA hardware:

When using DLA exports, some layers may not be supported to run on DLA and will fall back to the GPU for execution. This fallback can introduce additional latency and impact the overall inference performance. Therefore, DLA is not primarily designed to reduce inference latency compared to TensorRT running entirely on the GPU. Instead, its primary purpose is to increase throughput and improve energy efficiency.

YOLO11 benchmarks were run by the Ultralytics team on 11 different model formats measuring speed and accuracy: PyTorch, TorchScript, ONNX, OpenVINO, TensorRT, TF SavedModel, TF GraphDef, TF Lite, MNN, NCNN, ExecuTorch. Benchmarks were run on NVIDIA Jetson AGX Thor Developer Kit, NVIDIA Jetson AGX Orin Developer Kit (64GB), NVIDIA Jetson Orin Nano Super Developer Kit and Seeed Studio reComputer J4012 powered by Jetson Orin NX 16GB device at FP32 precision with default input image size of 640.

Even though all model exports work on NVIDIA Jetson, we have only included PyTorch, TorchScript, TensorRT for the comparison chart below because they make use of the GPU on the Jetson and are guaranteed to produce the best results. All the other exports only utilize the CPU and the performance is not as good as the above three. You can find benchmarks for all exports in the section after this chart.

The below table represents the benchmark results for five different models (YOLO11n, YOLO11s, YOLO11m, YOLO11l, YOLO11x) across 11 different formats (PyTorch, TorchScript, ONNX, OpenVINO, TensorRT, TF SavedModel, TF GraphDef, TF Lite, MNN, NCNN, ExecuTorch), giving us the status, size, mAP50-95(B) metric, and inference time for each combination.

Benchmarked with Ultralytics 8.3.226

Inference time does not include pre/ post-processing.

Benchmarked with Ultralytics 8.3.157

Inference time does not include pre/ post-processing.

Benchmarked with Ultralytics 8.3.157

Inference time does not include pre/ post-processing.

Benchmarked with Ultralytics 8.3.157

Inference time does not include pre/ post-processing.

Explore more benchmarking efforts by Seeed Studio running on different versions of NVIDIA Jetson hardware.

To reproduce the above Ultralytics benchmarks on all export formats run this code:

Note that benchmarking results might vary based on the exact hardware and software configuration of a system, as well as the current workload of the system at the time the benchmarks are run. For the most reliable results, use a dataset with a large number of images, e.g., data='coco.yaml' (5000 val images).

When using NVIDIA Jetson, there are a couple of best practices to follow in order to enable maximum performance on the NVIDIA Jetson running YOLO26.

Enable MAX Power Mode

Enabling MAX Power Mode on the Jetson will make sure all CPU, GPU cores are turned on.

Enabling Jetson Clocks will make sure all CPU, GPU cores are clocked at their maximum frequency.

Install Jetson Stats Application

We can use jetson stats application to monitor the temperatures of the system components and check other system details such as view CPU, GPU, RAM utilization, change power modes, set to max clocks, check JetPack information

For further learning and support, see the Ultralytics YOLO26 Docs.

Deploying Ultralytics YOLO26 on NVIDIA Jetson devices is a straightforward process. First, flash your Jetson device with the NVIDIA JetPack SDK. Then, either use a pre-built Docker image for quick setup or manually install the required packages. Detailed steps for each approach can be found in sections Quick Start with Docker and Start with Native Installation.

YOLO11 models have been benchmarked on various NVIDIA Jetson devices showing significant performance improvements. For example, the TensorRT format delivers the best inference performance. The table in the Detailed Comparison Tables section provides a comprehensive view of performance metrics like mAP50-95 and inference time across different model formats.

TensorRT is highly recommended for deploying YOLO26 models on NVIDIA Jetson due to its optimal performance. It accelerates inference by leveraging the Jetson's GPU capabilities, ensuring maximum efficiency and speed. Learn more about how to convert to TensorRT and run inference in the Use TensorRT on NVIDIA Jetson section.

To install PyTorch and Torchvision on NVIDIA Jetson, first uninstall any existing versions that may have been installed via pip. Then, manually install the compatible PyTorch and Torchvision versions for the Jetson's ARM64 architecture. Detailed instructions for this process are provided in the Install PyTorch and Torchvision section.

To maximize performance on NVIDIA Jetson with YOLO26, follow these best practices:

For commands and additional details, refer to the Best Practices when using NVIDIA Jetson section.

**Examples:**

Example 1 (bash):
```bash
t=ultralytics/ultralytics:latest-jetson-jetpack4
sudo docker pull $t && sudo docker run -it --ipc=host --runtime=nvidia $t
```

Example 2 (bash):
```bash
t=ultralytics/ultralytics:latest-jetson-jetpack5
sudo docker pull $t && sudo docker run -it --ipc=host --runtime=nvidia $t
```

Example 3 (bash):
```bash
t=ultralytics/ultralytics:latest-jetson-jetpack6
sudo docker pull $t && sudo docker run -it --ipc=host --runtime=nvidia $t
```

Example 4 (bash):
```bash
t=ultralytics/ultralytics:latest-nvidia-arm64
sudo docker pull $t && sudo docker run -it --ipc=host --runtime=nvidia $t
```

---

## Reference for ultralytics/solutions/streamlit_inference.py

**URL:** https://docs.ultralytics.com/reference/solutions/streamlit_inference/

**Contents:**
- Reference for ultralytics/solutions/streamlit_inference.py
- class ultralytics.solutions.streamlit_inference.Inference
  - method ultralytics.solutions.streamlit_inference.Inference.configure
  - method ultralytics.solutions.streamlit_inference.Inference.image_inference
  - method ultralytics.solutions.streamlit_inference.Inference.inference
  - method ultralytics.solutions.streamlit_inference.Inference.sidebar
  - method ultralytics.solutions.streamlit_inference.Inference.source_upload
  - method ultralytics.solutions.streamlit_inference.Inference.web_ui

This page is sourced from https://github.com/ultralytics/ultralytics/blob/main/ultralytics/solutions/streamlit_inference.py. Have an improvement or example to add? Open a Pull Request — thank you! 🙏

A class to perform object detection, image classification, image segmentation and pose estimation inference.

This class provides functionalities for loading models, configuring settings, uploading video files, and performing real-time inference using Streamlit and Ultralytics YOLO models.

Configure the model and load selected classes for inference.

Perform inference on uploaded images.

Perform real-time object detection inference on video or webcam feed.

Configure the Streamlit sidebar for model and inference settings.

Handle video file uploads through the Streamlit interface.

Set up the Streamlit web interface with custom HTML elements.

**Examples:**

Example 1 (swift):
```swift
Inference(self, **kwargs: Any) -> None
```

Example 2 (unknown):
```unknown
Create an Inference instance with a custom model
>>> inf = Inference(model="path/to/model.pt")
>>> inf.inference()

Create an Inference instance with default settings
>>> inf = Inference()
>>> inf.inference()
```

Example 3 (python):
```python
class Inference:
    """A class to perform object detection, image classification, image segmentation and pose estimation inference.

    This class provides functionalities for loading models, configuring settings, uploading video files, and performing
    real-time inference using Streamlit and Ultralytics YOLO models.

    Attributes:
        st (module): Streamlit module for UI creation.
        temp_dict (dict): Temporary dictionary to store the model path and other configuration.
        model_path (str): Path to the loaded model.
        model (YOLO): The YOLO model instance.
        source (str): Selected video source (webcam or video file).
        enable_trk (bool): Enable tracking option.
        conf (float): Confidence threshold for detection.
        iou (float): IoU threshold for non-maximum suppression.
        org_frame (Any): Container for the original frame to be displayed.
        ann_frame (Any): Container for the annotated frame to be displayed.
        vid_file_name (str | int): Name of the uploaded video file or webcam index.
        selected_ind (list[int]): List of selected class indices for detection.

    Methods:
        web_ui: Set up the Streamlit web interface with custom HTML elements.
        sidebar: Configure the Streamlit sidebar for model and inference settings.
        source_upload: Handle video file uploads through the Streamlit interface.
        configure: Configure the model and load selected classes for inference.
        inference: Perform real-time object detection inference.

    Examples:
        Create an Inference instance with a custom model
        >>> inf = Inference(model="path/to/model.pt")
        >>> inf.inference()

        Create an Inference instance with default settings
        >>> inf = Inference()
        >>> inf.inference()
    """

    def __init__(self, **kwargs: Any) -> None:
        """Initialize the Inference class, checking Streamlit requirements and setting up the model path.

        Args:
            **kwargs (Any): Additional keyword arguments for model configuration.
        """
        check_requirements("streamlit>=1.29.0")  # scope imports for faster ultralytics package load speeds
        import streamlit as st

        self.st = st  # Reference to the Streamlit module
        self.source = None  # Video source selection (webcam or video file)
        self.img_file_names = []  # List of image file names
        self.enable_trk = False  # Flag to toggle object tracking
        self.conf = 0.25  # Confidence threshold for detection
        self.iou = 0.45  # Intersection-over-Union (IoU) threshold for non-maximum suppression
        self.org_frame = None  # Container for the original frame display
        self.ann_frame = None  # Container for the annotated frame display
        self.vid_file_name = None  # Video file name or webcam index
        self.selected_ind: list[int] = []  # List of selected class indices for detection
        self.model = None  # YOLO model instance

        self.temp_dict = {"model": None, **kwargs}
        self.model_path = None  # Model file path
        if self.temp_dict["model"] is not None:
            self.model_path = self.temp_dict["model"]

        LOGGER.info(f"Ultralytics Solutions: ✅ {self.temp_dict}")
```

Example 4 (swift):
```swift
def configure(self) -> None
```

---

## Reference for ultralytics/__init__.py

**URL:** https://docs.ultralytics.com/ar/reference/__init__/

**Contents:**
- Reference for ultralytics/__init__.py
- function ultralytics.__getattr__
- function ultralytics.__dir__

This page is sourced from https://github.com/ultralytics/ultralytics/blob/main/ultralytics/__init__.py. Have an improvement or example to add? Open a Pull Request — thank you! 🙏

Lazy-import model classes on first access.

Extend dir() to include lazily available model names for IDE autocompletion.

**Examples:**

Example 1 (python):
```python
def __getattr__(name: str)
```

Example 2 (python):
```python
def __getattr__(name: str):
    """Lazy-import model classes on first access."""
    if name in MODELS:
        return getattr(importlib.import_module("ultralytics.models"), name)
    raise AttributeError(f"module {__name__} has no attribute {name}")
```

Example 3 (python):
```python
def __dir__()
```

Example 4 (python):
```python
def __dir__():
    """Extend dir() to include lazily available model names for IDE autocompletion."""
    return sorted(set(globals()) | set(MODELS))
```

---

## Reference for ultralytics/__init__.py

**URL:** https://docs.ultralytics.com/it/reference/__init__/

**Contents:**
- Reference for ultralytics/__init__.py
- function ultralytics.__getattr__
- function ultralytics.__dir__

This page is sourced from https://github.com/ultralytics/ultralytics/blob/main/ultralytics/__init__.py. Have an improvement or example to add? Open a Pull Request — thank you! 🙏

Lazy-import model classes on first access.

Extend dir() to include lazily available model names for IDE autocompletion.

**Examples:**

Example 1 (python):
```python
def __getattr__(name: str)
```

Example 2 (python):
```python
def __getattr__(name: str):
    """Lazy-import model classes on first access."""
    if name in MODELS:
        return getattr(importlib.import_module("ultralytics.models"), name)
    raise AttributeError(f"module {__name__} has no attribute {name}")
```

Example 3 (python):
```python
def __dir__()
```

Example 4 (python):
```python
def __dir__():
    """Extend dir() to include lazily available model names for IDE autocompletion."""
    return sorted(set(globals()) | set(MODELS))
```

---

## Reference for ultralytics/__init__.py

**URL:** https://docs.ultralytics.com/reference/__init__/

**Contents:**
- Reference for ultralytics/__init__.py
- function ultralytics.__getattr__
- function ultralytics.__dir__

This page is sourced from https://github.com/ultralytics/ultralytics/blob/main/ultralytics/__init__.py. Have an improvement or example to add? Open a Pull Request — thank you! 🙏

Lazy-import model classes on first access.

Extend dir() to include lazily available model names for IDE autocompletion.

**Examples:**

Example 1 (python):
```python
def __getattr__(name: str)
```

Example 2 (python):
```python
def __getattr__(name: str):
    """Lazy-import model classes on first access."""
    if name in MODELS:
        return getattr(importlib.import_module("ultralytics.models"), name)
    raise AttributeError(f"module {__name__} has no attribute {name}")
```

Example 3 (python):
```python
def __dir__()
```

Example 4 (python):
```python
def __dir__():
    """Extend dir() to include lazily available model names for IDE autocompletion."""
    return sorted(set(globals()) | set(MODELS))
```

---

## Rilevamento di oggetti

**URL:** https://docs.ultralytics.com/it/tasks/detect/

**Contents:**
- Rilevamento di oggetti
- Modelli
- Addestramento
  - Formato del set di dati
- Valutazione
- Predizione
- Esportazione
- FAQ
  - Come addestro un modello YOLO26 sul mio dataset personalizzato?
  - Quali modelli pre-addestrati sono disponibili in YOLO26?

Il rilevamento di oggetti è un'attività che implica l'identificazione della posizione e della classe degli oggetti in un'immagine o in un flusso video.

L'output di un rilevatore di oggetti è un insieme di bounding box che racchiudono gli oggetti nell'immagine, insieme alle etichette di classe e ai punteggi di confidenza per ogni box. Il rilevamento di oggetti è una buona scelta quando è necessario identificare oggetti di interesse in una scena, ma non è necessario sapere esattamente dove si trova l'oggetto o la sua forma esatta.

Guarda: Rilevamento di Oggetti con Modello Ultralytics YOLO Pre-addestrato.

I modelli YOLO26 Detect sono i modelli YOLO26 predefiniti, ovvero, yolo26n.pt, e sono pre-addestrati su COCO.

I modelli YOLO26 Detect pre-addestrati sono mostrati qui. I modelli Detect, Segment e Pose sono pre-addestrati sul dataset COCO, mentre i modelli Classify sono pre-addestrati sul dataset ImageNet.

I modelli vengono scaricati automaticamente dall'ultima release di Ultralytics al primo utilizzo.

Addestra YOLO26n sul dataset COCO8 per 100 epoche con dimensione immagine 640. Per un elenco completo degli argomenti disponibili, consulta la pagina Configurazione.

Il formato del dataset per il detection YOLO è descritto in dettaglio nella Guida al dataset. Per convertire il tuo dataset esistente da altri formati (come COCO ecc.) al formato YOLO, utilizza lo strumento JSON2YOLO di Ultralytics.

Convalida il modello YOLO26n addestrato accuratezza sul dataset COCO8. Non sono necessari argomenti poiché il model mantiene il suo training data e gli argomenti come attributi del modello.

Usa un modello YOLO26n addestrato per eseguire previsioni sulle immagini.

Vedi tutti i predict dettagli della modalità nella Predizione pagina.

Esporta un modello YOLO26n in un formato diverso come ONNX, CoreML, ecc.

I formati di esportazione YOLO26 disponibili sono nella tabella sottostante. Puoi esportare in qualsiasi formato usando il format argomento, cioè, format='onnx' oppure format='engine'. È possibile effettuare previsioni o validazioni direttamente sui modelli esportati, cioè, yolo predict model=yolo26n.onnx. Esempi di utilizzo vengono mostrati per il tuo modello dopo che l'esportazione è stata completata.

Vedi tutti i export dettagli nella Esportazione pagina.

L'addestramento di un modello YOLO26 su un dataset personalizzato comporta alcuni passaggi:

Per opzioni di configurazione dettagliate, visita la pagina Configurazione.

Ultralytics YOLO26 offre vari modelli pre-addestrati per il rilevamento di oggetti, la segmentazione e la stima della posa. Questi modelli sono pre-addestrati sul dataset COCO o su ImageNet per compiti di classificazione. Ecco alcuni dei modelli disponibili:

Per un elenco dettagliato e metriche di performance, consulta la sezione Modelli.

Per convalidare l'accuratezza del tuo modello YOLO26 addestrato, puoi usare il .val() metodo in python o il yolo detect val comando nella CLI. Questo fornirà metriche come mAP50-95, mAP50 e altro.

Per maggiori dettagli sulla convalida, visita la pagina Val.

Ultralytics YOLO26 consente di esportare i modelli in vari formati come ONNX, TensorRT, CoreML e altri per garantire la compatibilità tra diverse piattaforme e dispositivi.

Controlla l'elenco completo dei formati supportati e le istruzioni nella pagina Esporta.

Ultralytics YOLO26 è progettato per offrire prestazioni all'avanguardia per il rilevamento di oggetti, la segmentazione e la stima della posa. Ecco alcuni vantaggi chiave:

Esplora il nostro Blog per casi d'uso e storie di successo che mostrano YOLO26 in azione.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.yaml")  # build a new model from YAML
model = YOLO("yolo26n.pt")  # load a pretrained model (recommended for training)
model = YOLO("yolo26n.yaml").load("yolo26n.pt")  # build from YAML and transfer weights

# Train the model
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

Example 2 (sql):
```sql
# Build a new model from YAML and start training from scratch
yolo detect train data=coco8.yaml model=yolo26n.yaml epochs=100 imgsz=640

# Start training from a pretrained *.pt model
yolo detect train data=coco8.yaml model=yolo26n.pt epochs=100 imgsz=640

# Build a new model from YAML, transfer pretrained weights to it and start training
yolo detect train data=coco8.yaml model=yolo26n.yaml pretrained=yolo26n.pt epochs=100 imgsz=640
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load an official model
model = YOLO("path/to/best.pt")  # load a custom model

# Validate the model
metrics = model.val()  # no arguments needed, dataset and settings remembered
metrics.box.map  # map50-95
metrics.box.map50  # map50
metrics.box.map75  # map75
metrics.box.maps  # a list containing mAP50-95 for each category
```

Example 4 (unknown):
```unknown
yolo detect val model=yolo26n.pt      # val official model
yolo detect val model=path/to/best.pt # val custom model
```

---

## Security Alarm System Project Using Ultralytics YOLO26

**URL:** https://docs.ultralytics.com/guides/security-alarm-system/

**Contents:**
- Security Alarm System Project Using Ultralytics YOLO26
    - Email Received Sample
  - SecurityAlarm Arguments
- How It Works
- FAQ
  - How does Ultralytics YOLO26 improve the accuracy of a security alarm system?
  - Can I integrate Ultralytics YOLO26 with my existing security infrastructure?
  - What are the storage requirements for running Ultralytics YOLO26?
  - What makes Ultralytics YOLO26 different from other object detection models like Faster R-CNN or SSD?
  - How can I reduce the frequency of false positives in my security system using Ultralytics YOLO26?

The Security Alarm System Project utilizing Ultralytics YOLO26 integrates advanced computer vision capabilities to enhance security measures. YOLO26, developed by Ultralytics, provides real-time object detection, allowing the system to identify and respond to potential security threats promptly. This project offers several advantages:

Watch: Security Alarm System with Ultralytics YOLO26 + Solutions Object Detection

App Password Generation is necessary

Security Alarm System using Ultralytics YOLO

When you run the code, you will receive a single email notification if any object is detected. The notification is sent immediately, not repeatedly. You can customize the code to suit your project requirements.

Here's a table with the SecurityAlarm arguments:

The SecurityAlarm solution supports a variety of track parameters:

Moreover, the following visualization settings are available:

The Security Alarm System uses object tracking to monitor video feeds and detect potential security threats. When the system detects objects that exceed the specified threshold (set by the records parameter), it automatically sends an email notification with an image attachment showing the detected objects.

The system leverages the SecurityAlarm class which provides methods to:

This implementation is ideal for home security, retail surveillance, and other monitoring applications where immediate notification of detected objects is critical.

Ultralytics YOLO26 enhances security alarm systems by delivering high-accuracy, real-time object detection. Its advanced algorithms significantly reduce false positives, ensuring that the system only responds to genuine threats. This increased reliability can be seamlessly integrated with existing security infrastructure, upgrading the overall surveillance quality.

Yes, Ultralytics YOLO26 can be seamlessly integrated with your existing security infrastructure. The system supports various modes and provides flexibility for customization, allowing you to enhance your existing setup with advanced object detection capabilities. For detailed instructions on integrating YOLO26 in your projects, visit the integration section.

Running Ultralytics YOLO26 on a standard setup typically requires around 5GB of free disk space. This includes space for storing the YOLO26 model and any additional dependencies. For cloud-based solutions, Ultralytics Platform offers efficient project management and dataset handling, which can optimize storage needs. Learn more about the Pro Plan for enhanced features including extended storage.

Ultralytics YOLO26 provides an edge over models like Faster R-CNN or SSD with its real-time detection capabilities and higher accuracy. Its unique architecture allows it to process images much faster without compromising on precision, making it ideal for time-sensitive applications like security alarm systems. For a comprehensive comparison of object detection models, you can explore our guide.

To reduce false positives, ensure your Ultralytics YOLO26 model is adequately trained with a diverse and well-annotated dataset. Fine-tuning hyperparameters and regularly updating the model with new data can significantly improve detection accuracy. Detailed hyperparameter tuning techniques can be found in our hyperparameter tuning guide.

**Examples:**

Example 1 (python):
```python
import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("path/to/video.mp4")
assert cap.isOpened(), "Error reading video file"

# Video writer
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter("security_output.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

from_email = "abc@gmail.com"  # the sender email address
password = "---- ---- ---- ----"  # 16-digits password generated via: https://myaccount.google.com/apppasswords
to_email = "xyz@gmail.com"  # the receiver email address

# Initialize security alarm object
securityalarm = solutions.SecurityAlarm(
    show=True,  # display the output
    model="yolo26n.pt",  # e.g., yolo26s.pt, yolo26m.pt
    records=1,  # total detections count to send an email
)

securityalarm.authenticate(from_email, password, to_email)  # authenticate the email server

# Process video
while cap.isOpened():
    success, im0 = cap.read()

    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break

    results = securityalarm(im0)

    # print(results)  # access the output

    video_writer.write(results.plot_im)  # write the processed frame.

cap.release()
video_writer.release()
cv2.destroyAllWindows()  # destroy all opened windows
```

---

## Segmentazione delle istanze

**URL:** https://docs.ultralytics.com/it/tasks/segment/

**Contents:**
- Segmentazione delle istanze
- Modelli
- Addestramento
  - Formato del set di dati
- Valutazione
- Predizione
- Esportazione
- FAQ
  - Come si addestra un modello di segmentazione YOLO26 su un dataset personalizzato?
  - Qual è la differenza tra rilevamento di oggetti e segmentazione delle istanze in YOLO26?

L'instance segmentation fa un ulteriore passo avanti rispetto all'object detection e implica l'identificazione di singoli oggetti in un'immagine e la loro segmentazione dal resto dell'immagine.

L'output di un modello di instance segmentation è un insieme di maschere o contorni che delineano ciascun oggetto nell'immagine, insieme alle etichette di classe e ai punteggi di confidenza per ciascun oggetto. L'instance segmentation è utile quando è necessario sapere non solo dove si trovano gli oggetti in un'immagine, ma anche qual è la loro forma esatta.

Guarda: Esegui Segmentation con un modello Ultralytics YOLO pre-addestrato in Python.

I modelli YOLO26 Segment utilizzano il -seg suffisso, ad esempio, yolo26n-seg.pt, e sono pre-addestrati su COCO.

I modelli YOLO26 Segment pre-addestrati sono mostrati qui. I modelli Detect, Segment e Pose sono pre-addestrati sul dataset COCO, mentre i modelli Classify sono pre-addestrati sul dataset ImageNet.

I modelli vengono scaricati automaticamente dall'ultima release di Ultralytics al primo utilizzo.

Addestra YOLO26n-seg sul dataset COCO8-seg per 100 epoche con dimensione immagine 640. Per un elenco completo degli argomenti disponibili, consulta la pagina Configurazione.

Il formato del dataset per la segmentation YOLO è descritto in dettaglio nella Guida al dataset. Per convertire il tuo dataset esistente da altri formati (come COCO ecc.) al formato YOLO, utilizza lo strumento JSON2YOLO di Ultralytics.

Valida il modello YOLO26n-seg addestrato accuratezza sul dataset COCO8-seg. Non sono necessari argomenti poiché il model mantiene il suo training data e gli argomenti come attributi del modello.

Usa un modello YOLO26n-seg addestrato per eseguire predizioni su immagini.

Vedi tutti i predict dettagli della modalità nella Predizione pagina.

Esporta un modello YOLO26n-seg in un formato diverso come ONNX, CoreML, ecc.

I formati di esportazione YOLO26-seg disponibili sono nella tabella seguente. Puoi esportare in qualsiasi formato utilizzando il format argomento, cioè, format='onnx' oppure format='engine'. È possibile effettuare previsioni o validazioni direttamente sui modelli esportati, cioè, yolo predict model=yolo26n-seg.onnx. Esempi di utilizzo vengono mostrati per il tuo modello dopo che l'esportazione è stata completata.

Vedi tutti i export dettagli nella Esportazione pagina.

Per addestrare un modello di segmentazione YOLO26 su un dataset personalizzato, devi prima preparare il tuo dataset nel formato di segmentazione YOLO. Puoi utilizzare strumenti come JSON2YOLO per convertire dataset da altri formati. Una volta che il tuo dataset è pronto, puoi addestrare il modello utilizzando comandi Python o CLI:

Consulta la pagina Configurazione per ulteriori argomenti disponibili.

Il rilevamento di oggetti identifica e localizza gli oggetti all'interno di un'immagine disegnando bounding box attorno ad essi, mentre la segmentazione delle istanze non solo identifica i bounding box ma delinea anche la forma esatta di ciascun oggetto. I modelli di segmentazione delle istanze YOLO26 forniscono maschere o contorni che delineano ogni oggetto detect, il che è particolarmente utile per attività in cui conoscere la forma precisa degli oggetti è importante, come l'imaging medico o la guida autonoma.

Ultralytics YOLO26 è un modello all'avanguardia riconosciuto per la sua elevata precisione e le prestazioni in tempo reale, rendendolo ideale per i compiti di segmentazione delle istanze. I modelli YOLO26 Segment sono pre-addestrati sul dataset COCO, garantendo prestazioni robuste su una varietà di oggetti. Inoltre, YOLO supporta funzionalità di addestramento, validazione, predizione ed esportazione con integrazione perfetta, rendendolo altamente versatile sia per la ricerca che per le applicazioni industriali.

Caricare e convalidare un modello di segmentazione YOLO pre-addestrato è semplice. Ecco come puoi farlo usando sia Python che la CLI:

Questi passaggi ti forniranno metriche di convalida come la Mean Average Precision (mAP), fondamentali per valutare le prestazioni del modello.

Esportare un modello di segmentazione YOLO in formato ONNX è semplice e può essere fatto usando comandi Python o CLI:

Per maggiori dettagli sull'esportazione in vari formati, fare riferimento alla pagina Esportazione.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-seg.yaml")  # build a new model from YAML
model = YOLO("yolo26n-seg.pt")  # load a pretrained model (recommended for training)
model = YOLO("yolo26n-seg.yaml").load("yolo26n.pt")  # build from YAML and transfer weights

# Train the model
results = model.train(data="coco8-seg.yaml", epochs=100, imgsz=640)
```

Example 2 (sql):
```sql
# Build a new model from YAML and start training from scratch
yolo segment train data=coco8-seg.yaml model=yolo26n-seg.yaml epochs=100 imgsz=640

# Start training from a pretrained *.pt model
yolo segment train data=coco8-seg.yaml model=yolo26n-seg.pt epochs=100 imgsz=640

# Build a new model from YAML, transfer pretrained weights to it and start training
yolo segment train data=coco8-seg.yaml model=yolo26n-seg.yaml pretrained=yolo26n-seg.pt epochs=100 imgsz=640
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-seg.pt")  # load an official model
model = YOLO("path/to/best.pt")  # load a custom model

# Validate the model
metrics = model.val()  # no arguments needed, dataset and settings remembered
metrics.box.map  # map50-95(B)
metrics.box.map50  # map50(B)
metrics.box.map75  # map75(B)
metrics.box.maps  # a list containing mAP50-95(B) for each category
metrics.seg.map  # map50-95(M)
metrics.seg.map50  # map50(M)
metrics.seg.map75  # map75(M)
metrics.seg.maps  # a list containing mAP50-95(M) for each category
```

Example 4 (unknown):
```unknown
yolo segment val model=yolo26n-seg.pt  # val official model
yolo segment val model=path/to/best.pt # val custom model
```

---

## Semantic Image Search with OpenAI CLIP and Meta FAISS

**URL:** https://docs.ultralytics.com/guides/similarity-search/

**Contents:**
- Semantic Image Search with OpenAI CLIP and Meta FAISS
- Introduction
- Semantic Image Search Visual Preview
- How It Works
- VisualAISearch class
- VisualAISearch Parameters
- Advantages of Semantic Image Search with CLIP and FAISS
- FAQ
  - How does CLIP understand both images and text?
  - Why is CLIP considered so powerful for AI tasks?

This guide walks you through building a semantic image search engine using OpenAI CLIP, Meta FAISS, and Flask. By combining CLIP's powerful visual-language embeddings with FAISS's efficient nearest-neighbor search, you can create a fully functional web interface where you can retrieve relevant images using natural language queries.

Watch: How Similarity Search Works | Visual Search Using OpenAI CLIP, META FAISS and Ultralytics Package 🎉

This architecture supports zero-shot search, meaning you don't need labels or categories, just image data and a good prompt.

Semantic Image Search using Ultralytics Python package

If you're using your own images, make sure to provide an absolute path to the image directory. Otherwise, the images may not appear on the webpage due to Flask's file serving limitations.

This class performs all the backend operations:

Similar Images Search

If you're using your own images, make sure to provide an absolute path to the image directory. Otherwise, the images may not appear on the webpage due to Flask's file serving limitations.

The table below outlines the available parameters for VisualAISearch:

Building your own semantic image search system with CLIP and FAISS provides several compelling advantages:

Zero-Shot Capabilities: You don't need to train the model on your specific dataset. CLIP's zero-shot learning lets you perform search queries on any image dataset using free-form natural language, saving both time and resources.

Human-Like Understanding: Unlike keyword-based search engines, CLIP understands semantic context. It can retrieve images based on abstract, emotional, or relational queries like "a happy child in nature" or "a futuristic city skyline at night".

No Need for Labels or Metadata: Traditional image search systems require carefully labeled data. This approach only needs raw images. CLIP generates embeddings without needing any manual annotation.

Flexible and Scalable Search: FAISS enables fast nearest-neighbor search even with large-scale datasets. It's optimized for speed and memory, allowing real-time response even with thousands (or millions) of embeddings.

Cross-Domain Applications: Whether you're building a personal photo archive, a creative inspiration tool, a product search engine, or even an art recommendation system, this stack adapts to diverse domains with minimal tweaking.

CLIP (Contrastive Language Image Pretraining) is a model developed by OpenAI that learns to connect visual and linguistic information. It's trained on a massive dataset of images paired with natural language captions. This training allows it to map both images and text into a shared embedding space, so you can compare them directly using vector similarity.

What makes CLIP stand out is its ability to generalize. Instead of being trained just for specific labels or tasks, it learns from natural language itself. This allows it to handle flexible queries like “a man riding a jet ski” or “a surreal dreamscape,” making it useful for everything from classification to creative semantic search, without retraining.

FAISS (Facebook AI Similarity Search) is a toolkit that helps you search through high-dimensional vectors very efficiently. Once CLIP turns your images into embeddings, FAISS makes it fast and easy to find the closest matches to a text query, perfect for real-time image retrieval.

While CLIP and FAISS are developed by OpenAI and Meta respectively, the Ultralytics Python package simplifies their integration into a complete semantic image search pipeline in a 2-lines workflow that just works:

Similar Images Search

This high-level implementation handles:

Yes. The current setup uses Flask with a basic HTML frontend, but you can replace it with your own HTML or build a more dynamic UI with React, Vue, or another frontend framework. Flask can serve as the backend API for your custom interface.

Not directly. A simple workaround is to extract individual frames from your videos (e.g., one every second), treat them as standalone images, and feed those into the system. This way, the search engine can semantically index visual moments from your videos.

**Examples:**

Example 1 (python):
```python
from ultralytics import solutions

app = solutions.SearchApp(
    # data = "path/to/img/directory" # Optional, build search engine with your own images
    device="cpu"  # configure the device for processing, e.g., "cpu" or "cuda"
)

app.run(debug=False)  # You can also use `debug=True` argument for testing
```

Example 2 (python):
```python
from ultralytics import solutions

searcher = solutions.VisualAISearch(
    # data = "path/to/img/directory" # Optional, build search engine with your own images
    device="cuda"  # configure the device for processing, e.g., "cpu" or "cuda"
)

results = searcher("a dog sitting on a bench")

# Ranked Results:
#     - 000000546829.jpg | Similarity: 0.3269
#     - 000000549220.jpg | Similarity: 0.2899
#     - 000000517069.jpg | Similarity: 0.2761
#     - 000000029393.jpg | Similarity: 0.2742
#     - 000000534270.jpg | Similarity: 0.2680
```

Example 3 (python):
```python
from ultralytics import solutions

searcher = solutions.VisualAISearch(
    # data = "path/to/img/directory" # Optional, build search engine with your own images
    device="cuda"  # configure the device for processing, e.g., "cpu" or "cuda"
)

results = searcher("a dog sitting on a bench")

# Ranked Results:
#     - 000000546829.jpg | Similarity: 0.3269
#     - 000000549220.jpg | Similarity: 0.2899
#     - 000000517069.jpg | Similarity: 0.2761
#     - 000000029393.jpg | Similarity: 0.2742
#     - 000000534270.jpg | Similarity: 0.2680
```

---

## Soluzioni Ultralytics: Sfrutta YOLO26 per risolvere problemi del mondo reale

**URL:** https://docs.ultralytics.com/it/solutions/

**Contents:**
- Soluzioni Ultralytics: Sfrutta YOLO26 per risolvere problemi del mondo reale
- Soluzioni
  - Solutions Arguments
  - Utilizzo di SolutionAnnotator
  - Lavorare con SolutionResults
  - Solutions Usage via CLI
  - Contribuisci alle nostre soluzioni
- FAQ
  - Come posso utilizzare Ultralytics YOLO per il conteggio di oggetti in tempo reale?
  - Quali sono i vantaggi dell'utilizzo di Ultralytics YOLO per i sistemi di sicurezza?

Le soluzioni Ultralytics offrono applicazioni all'avanguardia dei modelli YOLO, fornendo soluzioni reali come il conteggio di oggetti, la sfocatura e i sistemi di sicurezza, migliorando l'efficienza e l'accuratezza in diversi settori. Scopri la potenza di YOLO26 per implementazioni pratiche e di impatto.

Guarda: Come eseguire le soluzioni Ultralytics dalla Riga di Comando (CLI) | Ultralytics YOLO26 🚀

Ecco la nostra lista curata di soluzioni Ultralytics che possono essere utilizzate per creare fantastici progetti di computer vision.

Traccia gli argomenti

Le soluzioni supportano anche alcuni degli argomenti da track, inclusi parametri come conf, line_width, tracker, model, show, verbose e classes.

Argomenti di visualizzazione

Puoi usare show_conf, show_labels, e altri argomenti menzionati per personalizzare la visualizzazione.

Tutte le Ultralytics Solutions utilizzano la classe separata SolutionAnnotator, che estende il principale Annotator class e hanno i seguenti metodi:

Eccetto Similarity Search, ogni chiamata a Solution restituisce un elenco di SolutionResults object.

SolutionResults object hanno i seguenti attributi:

Per maggiori dettagli, fare riferimento a SolutionResults documentazione della classe.

Informazioni sui comandi

La maggior parte delle soluzioni può essere utilizzata direttamente tramite l'interfaccia a riga di comando, tra cui:

Count, Crop, Blur, Workout, Heatmap, Isegment, Visioneye, Speed, Queue, Analytics, Inference

Accogliamo con favore i contributi della comunità! Se hai acquisito una particolare competenza in un aspetto di Ultralytics YOLO che non è ancora trattato nelle nostre soluzioni, ti incoraggiamo a condividere la tua esperienza. Scrivere una guida è un ottimo modo per dare qualcosa in cambio alla comunità e aiutarci a rendere la nostra documentazione più completa e facile da usare.

Per iniziare, leggi la nostra Guida per i contributi per le linee guida su come aprire una Pull Request (PR) 🛠️. Non vediamo l'ora di ricevere i tuoi contributi!

Lavoriamo insieme per rendere l'ecosistema Ultralytics YOLO più robusto e versatile 🙏!

Ultralytics YOLO26 può essere utilizzato per il conteggio di oggetti in tempo reale sfruttando le sue avanzate capacità di object detection. Puoi seguire la nostra guida dettagliata su Conteggio Oggetti per configurare YOLO26 per l'analisi di flussi video in diretta. Ti basta installare YOLO26, caricare il tuo modello e processare i fotogrammi video per contare gli oggetti dinamicamente.

Ultralytics YOLO26 migliora i sistemi di sicurezza offrendo object detection in tempo reale e meccanismi di allerta. Impiegando YOLO26, puoi creare un sistema di allarme di sicurezza che attiva avvisi quando nuovi oggetti vengono detect nell'area di sorveglianza. Scopri come configurare un Sistema di Allarme di Sicurezza con YOLO26 per un monitoraggio della sicurezza robusto.

Ultralytics YOLO26 può migliorare significativamente i sistemi di gestione delle code contando e track con precisione le persone in coda, contribuendo così a ridurre i tempi di attesa e ottimizzare l'efficienza del servizio. Segui la nostra guida dettagliata su Gestione Code per imparare come implementare YOLO26 per un monitoraggio e un'analisi efficaci delle code.

Sì, Ultralytics YOLO26 può essere efficacemente utilizzato per il monitoraggio degli allenamenti tramite il tracking e l'analisi delle routine di fitness in tempo reale. Ciò consente una valutazione precisa della forma e delle prestazioni degli esercizi. Esplora la nostra guida su Monitoraggio Allenamenti per imparare come configurare un sistema di monitoraggio degli allenamenti basato su AI utilizzando YOLO26.

Ultralytics YOLO26 può generare heatmap per visualizzare l'intensità dei dati in una data area, evidenziando regioni di alta attività o interesse. Questa funzionalità è particolarmente utile per comprendere schemi e tendenze in vari compiti di computer vision. Scopri di più sulla creazione e l'utilizzo di Heatmap con YOLO26 per un'analisi e visualizzazione completa dei dati.

**Examples:**

Example 1 (python):
```python
import cv2

from ultralytics import solutions

im0 = cv2.imread("path/to/img")

region_points = [(20, 400), (1080, 400), (1080, 360), (20, 360)]

counter = solutions.ObjectCounter(
    show=True,  # display the output
    region=region_points,  # pass region points
    model="yolo26n.pt",  # model="yolo26n-obb.pt" for object counting with OBB model.
    # classes=[0, 2],  # count specific classes i.e. person and car with COCO pretrained model.
    # tracker="botsort.yaml"  # Choose trackers i.e "bytetrack.yaml"
)
results = counter(im0)
print(results.in_count)  # display in_counts
print(results.out_count)  # display out_counts
print(results.classwise_count)  # display classwise_count
```

Example 2 (unknown):
```unknown
yolo SOLUTIONS SOLUTION_NAME ARGS
```

Example 3 (unknown):
```unknown
yolo solutions count show=True # for object counting

yolo solutions count source="path/to/video.mp4" # specify video file path
```

---

## Stima della posa

**URL:** https://docs.ultralytics.com/it/tasks/pose/

**Contents:**
- Stima della posa
- Modelli
- Addestramento
  - Formato del set di dati
- Valutazione
- Predizione
- Esportazione
- FAQ
  - Cos'è la stima della posa con Ultralytics YOLO26 e come funziona?
  - Come posso addestrare un modello YOLO26-pose su un dataset personalizzato?

La stima della posa è un'attività che prevede l'identificazione della posizione di punti specifici in un'immagine, solitamente indicati come keypoint. I keypoint possono rappresentare varie parti dell'oggetto, come giunture, punti di riferimento o altre caratteristiche distintive. Le posizioni dei keypoint sono generalmente rappresentate come un insieme di coordinate 2D [x, y] o 3D [x, y, visible] coordinate.

L'output di un modello di stima della posa è un insieme di punti che rappresentano i keypoint su un oggetto nell'immagine, solitamente insieme ai punteggi di confidenza per ciascun punto. La stima della posa è una buona scelta quando è necessario identificare parti specifiche di un oggetto in una scena e la loro posizione in relazione tra loro.

Guarda: Tutorial sulla stima della posa con Ultralytics YOLO26 | Tracciamento di oggetti in tempo reale e Rilevamento della posa umana

YOLO26 pose i modelli utilizzano il -pose suffisso, ad esempio, yolo26n-pose.pt. Questi modelli sono addestrati sul Keypoints COCO e sono adatti per una varietà di attività di stima della posa.

Nel modello di posa YOLO26 predefinito, ci sono 17 keypoints, ciascuno rappresentante una diversa parte del corpo umano. Ecco la mappatura di ogni indice al rispettivo giunto corporeo:

I modelli di posa pre-addestrati Ultralytics YOLO26 sono mostrati qui. I modelli Detect, Segment e Pose sono pre-addestrati sul dataset COCO, mentre i modelli Classify sono pre-addestrati sul dataset ImageNet.

I modelli vengono scaricati automaticamente dall'ultima release di Ultralytics al primo utilizzo.

Addestra un modello YOLO26-pose sul dataset COCO8-pose. Il dataset COCO8-pose è un piccolo dataset di esempio perfetto per testare e debuggare i tuoi modelli di stima della posa.

Il formato del dataset per il pose YOLO è descritto in dettaglio nella Guida al dataset. Per convertire il tuo dataset esistente da altri formati (come COCO ecc.) al formato YOLO, utilizza lo strumento JSON2YOLO di Ultralytics.

Per attività personalizzate di stima della posa, puoi anche esplorare set di dati specializzati come Tiger-Pose per la stima della posa degli animali, Hand Keypoints per il tracciamento della mano o Dog-Pose per l'analisi della posa canina.

Convalida il modello YOLO26n-pose addestrato accuratezza sul dataset COCO8-pose. Non sono necessari argomenti poiché il model mantiene il suo training data e gli argomenti come attributi del modello.

Utilizza un modello YOLO26n-pose addestrato per eseguire predizioni su immagini. La modalità predict ti consente di eseguire inferenze su immagini, video o stream in tempo reale.

Vedi tutti i predict dettagli della modalità nella Predizione pagina.

Esporta un modello YOLO26n Pose in un formato diverso come ONNX, CoreML, ecc. Questo ti consente di distribuire il tuo modello su varie piattaforme e dispositivi per l'inferenza in tempo reale.

I formati di esportazione YOLO26-pose disponibili sono nella tabella sottostante. Puoi esportare in qualsiasi formato utilizzando il format argomento, cioè, format='onnx' oppure format='engine'. È possibile effettuare previsioni o validazioni direttamente sui modelli esportati, cioè, yolo predict model=yolo26n-pose.onnx. Esempi di utilizzo vengono mostrati per il tuo modello dopo che l'esportazione è stata completata.

Vedi tutti i export dettagli nella Esportazione pagina.

La stima della posa con Ultralytics YOLO26 implica l'identificazione di punti specifici, noti come keypoints, in un'immagine. Questi keypoints rappresentano tipicamente articolazioni o altre caratteristiche importanti dell'oggetto. L'output include le [x, y] coordinate e punteggi di confidenza per ogni punto. I modelli YOLO26-pose sono specificamente progettati per questo compito e utilizzano il -pose suffisso, come yolo26n-pose.pt. Questi modelli sono pre-addestrati su dataset come Keypoints COCO e possono essere utilizzati per varie attività di stima della posa. Per maggiori informazioni, visita la Pagina sulla Stima della Posa.

L'addestramento di un modello YOLO26-pose su un dataset personalizzato implica il caricamento di un modello, che può essere un nuovo modello definito da un file yaml o un modello pre-addestrato. È quindi possibile avviare il processo di addestramento utilizzando il dataset e i parametri specificati.

Per dettagli completi sull'addestramento, fare riferimento alla Sezione Addestramento. È inoltre possibile utilizzare la Piattaforma Ultralytics per un approccio senza codice all'addestramento di modelli personalizzati di stima della posa.

La validazione di un modello YOLO26-pose implica la valutazione della sua accuratezza utilizzando gli stessi parametri del dataset mantenuti durante l'addestramento. Ecco un esempio:

Per maggiori informazioni, visita la Sezione Val.

Sì, è possibile esportare un modello YOLO26-pose in vari formati come ONNX, CoreML, TensorRT e altri. Questo può essere fatto utilizzando python o l'interfaccia a riga di comando (CLI).

Per maggiori dettagli, fare riferimento alla Sezione Esportazione. I modelli esportati possono essere implementati su dispositivi edge per applicazioni in tempo reale come il monitoraggio della forma fisica, l'analisi sportiva o la robotica.

Ultralytics YOLO26 offre vari modelli pose pre-addestrati come YOLO26n-pose, YOLO26s-pose, YOLO26m-pose, tra gli altri. Questi modelli differiscono per dimensioni, accuratezza (mAP) e velocità. Ad esempio, il modello YOLO26n-pose raggiunge un mAPpose50-95 di 50.0 e un mAPpose50 di 81.0. Per un elenco completo e dettagli sulle prestazioni, visitare la Sezione Modelli.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-pose.yaml")  # build a new model from YAML
model = YOLO("yolo26n-pose.pt")  # load a pretrained model (recommended for training)
model = YOLO("yolo26n-pose.yaml").load("yolo26n-pose.pt")  # build from YAML and transfer weights

# Train the model
results = model.train(data="coco8-pose.yaml", epochs=100, imgsz=640)
```

Example 2 (sql):
```sql
# Build a new model from YAML and start training from scratch
yolo pose train data=coco8-pose.yaml model=yolo26n-pose.yaml epochs=100 imgsz=640

# Start training from a pretrained *.pt model
yolo pose train data=coco8-pose.yaml model=yolo26n-pose.pt epochs=100 imgsz=640

# Build a new model from YAML, transfer pretrained weights to it and start training
yolo pose train data=coco8-pose.yaml model=yolo26n-pose.yaml pretrained=yolo26n-pose.pt epochs=100 imgsz=640
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-pose.pt")  # load an official model
model = YOLO("path/to/best.pt")  # load a custom model

# Validate the model
metrics = model.val()  # no arguments needed, dataset and settings remembered
metrics.box.map  # map50-95
metrics.box.map50  # map50
metrics.box.map75  # map75
metrics.box.maps  # a list containing mAP50-95 for each category
metrics.pose.map  # map50-95(P)
metrics.pose.map50  # map50(P)
metrics.pose.map75  # map75(P)
metrics.pose.maps  # a list containing mAP50-95(P) for each category
```

Example 4 (unknown):
```unknown
yolo pose val model=yolo26n-pose.pt # val official model
yolo pose val model=path/to/best.pt # val custom model
```

---

## Task di Visione Artificiale Supportati da Ultralytics YOLO26

**URL:** https://docs.ultralytics.com/it/tasks/

**Contents:**
- Task di Visione Artificiale Supportati da Ultralytics YOLO26
- Rilevamento
- Segmentazione delle immagini
- Classificazione
- Stima della posa
- OBB
- Conclusione
- FAQ
  - Quali task di visione artificiale può eseguire Ultralytics YOLO26?
  - Come si usa Ultralytics YOLO26 per il rilevamento di oggetti?

Ultralytics YOLO26 è un framework di intelligenza artificiale versatile che supporta molteplici attività di visione artificiale. Il framework può essere utilizzato per eseguire rilevamento, segmentazione, OBB, classificazione e stima della posa. Ciascuna di queste attività ha un obiettivo e un caso d'uso diversi, consentendo di affrontare varie sfide di visione artificiale con un unico framework.

Guarda: Esplora le attività di Ultralytics YOLO: Rilevamento di oggetti, Segmentazione, OBB, Tracking e Stima della Posa.

Il rilevamento è l'attività principale supportata da YOLO26. Implica l'identificazione di oggetti in un'immagine o in un frame video e il disegno di bounding box attorno ad essi. Gli oggetti rilevati vengono classificati in diverse categorie in base alle loro caratteristiche. YOLO26 può rilevare più oggetti in una singola immagine o frame video con elevata precisione e velocità, rendendolo ideale per applicazioni in tempo reale come i sistemi di sorveglianza e i veicoli autonomi.

Esempi di rilevamento

La segmentazione porta il rilevamento di oggetti oltre, producendo maschere a livello di pixel per ogni oggetto. Questa precisione è utile per applicazioni come l'imaging medico, l'analisi agricola e il controllo qualità nella produzione.

Esempi di segmentazione

La classificazione implica la categorizzazione di intere immagini in base al loro contenuto. Questo compito è essenziale per applicazioni come la categorizzazione dei prodotti nell'e-commerce, la moderazione dei contenuti e il monitoraggio della fauna selvatica.

Esempi di classificazione

La stima della posa rileva punti chiave specifici in immagini o frame video per tracciare movimenti o stimare pose. Questi punti chiave possono rappresentare articolazioni umane, tratti del viso o altri punti di interesse significativi. YOLO26 eccelle nel rilevamento dei punti chiave con elevata precisione e velocità, rendendolo prezioso per le applicazioni per il fitness, l'analisi sportiva e l'interazione uomo-computer.

Il rilevamento di Bounding Box Orientate (OBB) migliora il tradizionale rilevamento di oggetti aggiungendo un angolo di orientamento per localizzare meglio gli oggetti ruotati. Questa capacità è particolarmente preziosa per l'analisi di immagini aeree, l'elaborazione di documenti e le applicazioni industriali dove gli oggetti appaiono con varie angolazioni. YOLO26 offre elevata precisione e velocità per rilevare oggetti ruotati in diversi scenari.

Rilevamento orientato

Ultralytics YOLO26 supporta molteplici attività di visione artificiale, tra cui rilevamento, segmentazione, classificazione, rilevamento di oggetti orientati e rilevamento dei punti chiave. Ogni attività risponde a esigenze specifiche nel panorama della visione artificiale, dall'identificazione di base degli oggetti all'analisi dettagliata della posa. Comprendendo le capacità e le applicazioni di ciascuna attività, è possibile selezionare l'approccio più appropriato per le proprie sfide specifiche di visione artificiale e sfruttare le potenti funzionalità di YOLO26 per costruire soluzioni efficaci.

Ultralytics YOLO26 è un framework AI versatile in grado di eseguire vari task di visione artificiale con elevata precisione e velocità. Questi task includono:

Per utilizzare Ultralytics YOLO26 per il rilevamento di oggetti, seguire questi passaggi:

Per istruzioni più dettagliate, consulta i nostri esempi di rilevamento.

L'utilizzo di YOLO26 per le attività di segmentazione offre numerosi vantaggi:

Scopri di più sui vantaggi e i casi d'uso di YOLO26 per la segmentazione nella sezione di segmentazione delle immagini.

Sì, Ultralytics YOLO26 può eseguire efficacemente la stima della posa e il rilevamento dei punti chiave con elevata precisione e velocità. Questa funzionalità è particolarmente utile per tracciare movimenti nelle analisi sportive, nella sanità e nelle applicazioni di interazione uomo-computer. YOLO26 rileva i punti chiave in un'immagine o in un frame video, consentendo una stima precisa della posa.

Per maggiori dettagli e suggerimenti sull'implementazione, visita i nostri esempi di stima della posa.

Il Rilevamento di Oggetti Orientati (OBB) con YOLO26 offre una precisione migliorata rilevando oggetti con un parametro angolare aggiuntivo. Questa funzionalità è vantaggiosa per applicazioni che richiedono una localizzazione accurata di oggetti ruotati, come l'analisi di immagini aeree e l'automazione di magazzini.

Consulta la sezione sul rilevamento di oggetti orientati per maggiori dettagli ed esempi.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a pretrained YOLO model (adjust model type as needed)
model = YOLO("yolo26n.pt")  # n, s, m, l, x versions available

# Perform object detection on an image
results = model.predict(source="image.jpg")  # Can also use video, directory, URL, etc.

# Display the results
results[0].show()  # Show the first image results
```

Example 2 (sql):
```sql
# Run YOLO detection from the command line
yolo detect model=yolo26n.pt source="image.jpg" # Adjust model and source as needed
```

---

## Tracking Multi-Oggetto con Ultralytics YOLO

**URL:** https://docs.ultralytics.com/it/modes/track/

**Contents:**
- Tracking Multi-Oggetto con Ultralytics YOLO
- Perché scegliere Ultralytics YOLO per il tracking degli oggetti?
- Applicazioni nel mondo reale
- Caratteristiche in sintesi
- Tracker disponibili
- Tracking
- Configurazione
  - Argomenti di Tracking
  - Selezione del Tracker
  - Argomenti del tracker

Il tracking degli oggetti nel campo della video analisi è un'attività fondamentale che non solo identifica la posizione e la classe degli oggetti all'interno del fotogramma, ma mantiene anche un ID univoco per ogni oggetto rilevato man mano che il video avanza. Le applicazioni sono illimitate, che vanno dalla sorveglianza e sicurezza all'analisi sportiva in tempo reale.

L'output dei tracker Ultralytics è coerente con l'object detection standard, ma ha il valore aggiunto degli ID oggetto. Questo semplifica il track degli oggetti nei flussi video e l'esecuzione di analisi successive. Ecco perché dovresti considerare l'utilizzo di Ultralytics YOLO per le tue esigenze di object tracking:

Guarda: Rilevamento e tracciamento di oggetti con Ultralytics YOLO.

Ultralytics YOLO estende le sue funzionalità di rilevamento oggetti per fornire un tracciamento oggetti solido e versatile:

Ultralytics YOLO supporta i seguenti algoritmi di tracciamento. Possono essere abilitati passando il file di configurazione YAML pertinente, come ad esempio tracker=tracker_type.yaml:

Il tracker predefinito è BoT-SORT.

Per eseguire il tracker su stream video, utilizzare un modello Detect, Segment o Pose addestrato come YOLO26n, YOLO26n-seg o YOLO26n-pose.

Come si può vedere nell'utilizzo sopra, il tracking è disponibile per tutti i modelli Detect, Segment e Pose eseguiti su video o sorgenti di streaming.

La configurazione del tracciamento condivide le proprietà con la modalità Predict, come ad esempio conf, iou, e show. Per ulteriori configurazioni, fare riferimento alla Predizione pagina del modello.

Ultralytics ti consente anche di utilizzare un file di configurazione del tracker modificato. Per fare ciò, è sufficiente fare una copia di un file di configurazione del tracker (ad esempio, custom_tracker.yaml) da ultralytics/cfg/trackers e modificare qualsiasi configurazione (ad eccezione di tracker_type) in base alle proprie esigenze.

Fare riferimento alla sezione Argomenti Tracker per una descrizione dettagliata di ciascun parametro.

Alcuni comportamenti di tracking possono essere ottimizzati modificando i file di configurazione YAML specifici per ogni algoritmo di tracking. Questi file definiscono parametri come soglie, buffer e logica di corrispondenza:

La tabella seguente fornisce una descrizione di ciascun parametro:

Informazioni sulla soglia del tracker

Se il punteggio di confidenza di un detect scende al di sotto di track_high_thresh, il tracker non aggiornerà quell'oggetto, risultando in nessuna traccia attiva.

Per impostazione predefinita, ReID è disattivato per ridurre al minimo il sovraccarico delle prestazioni. Abilitarlo è semplice: basta impostare with_reid: True nel configurazione del tracker. Puoi anche personalizzare il model utilizzato per ReID, consentendo di bilanciare accuratezza e velocità a seconda del caso d'uso:

Per prestazioni migliori, soprattutto quando si utilizza un modello di classificazione separato per ReID, è possibile esportarlo in un backend più veloce come TensorRT:

Esportazione di un modello ReID in TensorRT

Una volta esportato, puoi puntare al percorso del modello TensorRT nella configurazione del tuo tracker e verrà utilizzato per il ReID durante il tracking.

Guarda: Come creare un sistema interattivo di object tracking con Ultralytics YOLO | Clicca per ritagliare e visualizzare ⚡

Ecco uno script python che utilizza OpenCV (cv2) e YOLO26 per eseguire il tracking degli oggetti sui frame video. Questo script presuppone che i pacchetti necessari (opencv-python e ultralytics) siano già installati. Il persist=True indica al tracker che l'immagine o il fotogramma corrente è il successivo in una sequenza e di prevedere le tracce dall'immagine precedente nell'immagine corrente.

Ciclo for di streaming con tracciamento

Si prega di notare la modifica da model(frame) a model.track(frame), che abilita il tracciamento degli oggetti invece della semplice rilevazione. Questo script modificato eseguirà il tracker su ogni fotogramma del video, visualizzerà i risultati e li mostrerà in una finestra. È possibile uscire dal ciclo premendo 'q'.

La visualizzazione delle tracce degli oggetti su frame consecutivi può fornire preziose informazioni sui modelli di movimento e sul comportamento degli oggetti detect all'interno di un video. Con Ultralytics YOLO26, la rappresentazione grafica di queste tracce è un processo semplice ed efficiente.

Nell'esempio seguente, dimostriamo come utilizzare le capacità di tracking di YOLO26 per rappresentare graficamente il movimento degli oggetti detect attraverso più frame video. Questo script prevede l'apertura di un file video, la sua lettura frame per frame e l'utilizzo del modello YOLO per identificare e track vari oggetti. Mantenendo i punti centrali dei bounding box detect e collegandoli, possiamo disegnare linee che rappresentano i percorsi seguiti dagli oggetti track.

Tracciamento delle tracce su più fotogrammi video

Il tracciamento multithread offre la possibilità di eseguire il tracciamento degli oggetti su più flussi video contemporaneamente. Ciò è particolarmente utile quando si gestiscono più input video, ad esempio da più telecamere di sorveglianza, dove l'elaborazione concorrente può migliorare notevolmente l'efficienza e le prestazioni.

Nello script python fornito, utilizziamo il modulo threading di python per eseguire più istanze del tracker contemporaneamente. Ogni thread è responsabile dell'esecuzione del tracker su un file video e tutti i thread vengono eseguiti simultaneamente in background.

Per garantire che ogni thread riceva i parametri corretti (il file video, il modello da utilizzare e l'indice del file), definiamo una funzione run_tracker_in_thread che accetta questi parametri e contiene il ciclo di tracciamento principale. Questa funzione legge il video fotogramma per fotogramma, esegue il tracker e visualizza i risultati.

In questo esempio vengono utilizzati due modelli diversi: yolo26n.pt e yolo26n-seg.pt, ciascuno dei quali traccia gli oggetti in un file video diverso. I file video sono specificati in SOURCES.

Il daemon=True parametro in threading.Thread significa che questi thread verranno chiusi non appena il programma principale termina. Avviamo quindi i thread con start() e usiamo join() per fare in modo che il thread principale attenda fino al termine di entrambi i thread del tracker.

Infine, dopo che tutti i thread hanno completato il loro compito, le finestre che mostrano i risultati vengono chiuse usando cv2.destroyAllWindows().

Implementazione del tracking multithreaded

Questo esempio può essere facilmente esteso per gestire più file video e modelli creando più thread e applicando la stessa metodologia.

Hai esperienza nel multi-object tracking e hai implementato o adattato con successo un algoritmo di tracking con Ultralytics YOLO? Ti invitiamo a contribuire alla nostra sezione Trackers in ultralytics/cfg/trackers! Le tue applicazioni e soluzioni nel mondo reale potrebbero essere preziose per gli utenti che lavorano su attività di tracking.

Contribuendo a questa sezione, aiuti ad ampliare la portata delle soluzioni di tracking disponibili all'interno del framework Ultralytics YOLO, aggiungendo un ulteriore livello di funzionalità e utilità per la comunità.

Per iniziare il tuo contributo, consulta la nostra Guida per i contributi per istruzioni complete sull'invio di una Pull Request (PR) 🛠️. Siamo entusiasti di vedere cosa porterai!

Insieme, miglioriamo le capacità di tracking dell'ecosistema Ultralytics YOLO 🙏!

Il tracciamento multi-oggetto nell'analisi video implica sia l'identificazione degli oggetti sia il mantenimento di un ID univoco per ciascun oggetto rilevato nei fotogrammi video. Ultralytics YOLO supporta questo fornendo il tracciamento in tempo reale insieme agli ID oggetto, facilitando attività come la sorveglianza di sicurezza e l'analisi sportiva. Il sistema utilizza tracker come BoT-SORT e ByteTrack, che possono essere configurati tramite file YAML.

È possibile configurare un tracker personalizzato copiando un file di configurazione del tracker esistente (ad esempio, custom_tracker.yaml) dalla directory di configurazione del tracker Ultralytics e modificando i parametri in base alle esigenze, ad eccezione di. tracker_typeUsa questo file nel tuo modello di tracking in questo modo:

Per eseguire l'object tracking su più flussi video contemporaneamente, puoi usare il modulo threading di python. Ogni thread gestirà un flusso video separato. Ecco un esempio di come puoi impostarlo:

Tracking Multithreaded

Il multi-object tracking con Ultralytics YOLO ha numerose applicazioni, tra cui:

Queste applicazioni beneficiano della capacità di Ultralytics YOLO di elaborare video ad alta frequenza di fotogrammi in tempo reale con un'eccezionale accuratezza.

Per visualizzare i track degli oggetti su più frame video, è possibile utilizzare le funzionalità di tracking del modello YOLO insieme a OpenCV per disegnare i percorsi degli oggetti rilevati. Ecco uno script di esempio che lo dimostra:

Tracciamento delle tracce su più fotogrammi video

Questo script traccerà le linee di tracciamento che mostrano i percorsi di movimento degli oggetti tracciati nel tempo, fornendo preziose informazioni sul comportamento e sui modelli degli oggetti.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load an official or custom model
model = YOLO("yolo26n.pt")  # Load an official Detect model
model = YOLO("yolo26n-seg.pt")  # Load an official Segment model
model = YOLO("yolo26n-pose.pt")  # Load an official Pose model
model = YOLO("path/to/best.pt")  # Load a custom-trained model

# Perform tracking with the model
results = model.track("https://youtu.be/LNwODJXcvt4", show=True)  # Tracking with default tracker
results = model.track("https://youtu.be/LNwODJXcvt4", show=True, tracker="bytetrack.yaml")  # with ByteTrack
```

Example 2 (julia):
```julia
# Perform tracking with various models using the command line interface
yolo track model=yolo26n.pt source="https://youtu.be/LNwODJXcvt4"      # Official Detect model
yolo track model=yolo26n-seg.pt source="https://youtu.be/LNwODJXcvt4"  # Official Segment model
yolo track model=yolo26n-pose.pt source="https://youtu.be/LNwODJXcvt4" # Official Pose model
yolo track model=path/to/best.pt source="https://youtu.be/LNwODJXcvt4" # Custom trained model

# Track using ByteTrack tracker
yolo track model=path/to/best.pt source="https://youtu.be/LNwODJXcvt4" tracker="bytetrack.yaml"
```

Example 3 (python):
```python
from ultralytics import YOLO

# Configure the tracking parameters and run the tracker
model = YOLO("yolo26n.pt")
results = model.track(source="https://youtu.be/LNwODJXcvt4", conf=0.1, iou=0.7, show=True)
```

Example 4 (julia):
```julia
# Configure tracking parameters and run the tracker using the command line interface
yolo track model=yolo26n.pt source="https://youtu.be/LNwODJXcvt4" conf=0.1 iou=0.7 show
```

---

## Training YOLO26 with ClearML: Streamlining Your MLOps Workflow

**URL:** https://docs.ultralytics.com/integrations/clearml/

**Contents:**
- Training YOLO26 with ClearML: Streamlining Your MLOps Workflow
- ClearML
- YOLO26 Training with ClearML
- Installation
- Configuring ClearML
- Usage
  - Understanding the Code
  - Understanding the Output
  - Viewing the ClearML Results Page
    - Key Features of the ClearML Results Page

MLOps bridges the gap between creating and deploying machine learning models in real-world settings. It focuses on efficient deployment, scalability, and ongoing management to ensure models perform well in practical applications.

Ultralytics YOLO26 effortlessly integrates with ClearML, streamlining and enhancing your object detection model's training and management. This guide will walk you through the integration process, detailing how to set up ClearML, manage experiments, automate model management, and collaborate effectively.

ClearML is an innovative open-source MLOps platform that is skillfully designed to automate, monitor, and orchestrate machine learning workflows. Its key features include automated logging of all training and inference data for full experiment reproducibility, an intuitive web UI for easy data visualization and analysis, advanced hyperparameter optimization algorithms, and robust model management for efficient deployment across various platforms.

You can bring automation and efficiency to your machine learning workflow by integrating YOLO26 with ClearML to improve your training process.

To install the required packages, run:

For detailed instructions and best practices related to the installation process, be sure to check our YOLO26 Installation guide. While installing the required packages for YOLO26, if you encounter any difficulties, consult our Common Issues guide for solutions and tips.

Once you have installed the necessary packages, the next step is to initialize and configure your ClearML SDK. This involves setting up your ClearML account and obtaining the necessary credentials for a seamless connection between your development environment and the ClearML server.

Begin by initializing the ClearML SDK in your environment. The clearml-init command starts the setup process and prompts you for the necessary credentials.

After executing this command, visit the ClearML Settings page. Navigate to the top right corner and select "Settings." Go to the "Workspace" section and click on "Create new credentials." Use the credentials provided in the "Create Credentials" pop-up to complete the setup as instructed, depending on whether you are configuring ClearML in a Jupyter Notebook or a local Python environment.

Before diving into the usage instructions, be sure to check out the range of YOLO26 models offered by Ultralytics. This will help you choose the most appropriate model for your project requirements.

Let's understand the steps showcased in the usage code snippet above.

Step 1: Creating a ClearML Task: A new task is initialized in ClearML, specifying your project and task names. This task will track and manage your model's training.

Step 2: Selecting the YOLO26 Model: The model_variant variable is set to 'yolo26n', one of the YOLO26 models. This variant is then logged in ClearML for tracking.

Step 3: Loading the YOLO26 Model: The selected YOLO26 model is loaded using Ultralytics' YOLO class, preparing it for training.

Step 4: Setting Up Training Arguments: Key training arguments like the dataset (coco8.yaml) and the number of epochs (16) are organized in a dictionary and connected to the ClearML task. This allows for tracking and potential modification via the ClearML UI. For a detailed understanding of the model training process and best practices, refer to our YOLO26 Model Training guide.

Step 5: Initiating Model Training: The model training is started with the specified arguments. The results of the training process are captured in the results variable.

Upon running the usage code snippet above, you can expect the following output:

By clicking on the URL link to the ClearML results page in the output of the usage code snippet, you can access a comprehensive view of your model's training process.

Real-Time Metrics Tracking

Experiment Comparison

Detailed Logs and Outputs

Resource Utilization Monitoring

Model Artifacts Management

For a visual walkthrough of what the ClearML Results Page looks like, watch the video below:

Watch: YOLO26 MLOps Integration using ClearML

ClearML offers several advanced features to enhance your MLOps experience.

ClearML's remote execution feature facilitates the reproduction and manipulation of experiments on different machines. It logs essential details like installed packages and uncommitted changes. When a task is enqueued, the ClearML Agent pulls it, recreates the environment, and runs the experiment, reporting back with detailed results.

Deploying a ClearML Agent is straightforward and can be done on various machines using the following command:

This setup is applicable to cloud VMs, local GPUs, or laptops. ClearML Autoscalers help manage cloud workloads on platforms like AWS, GCP, and Azure, automating the deployment of agents and adjusting resources based on your resource budget.

ClearML's user-friendly interface allows easy cloning, editing, and enqueuing of tasks. Users can clone an existing experiment, adjust parameters or other details through the UI, and enqueue the task for execution. This streamlined process ensures that the ClearML Agent executing the task uses updated configurations, making it ideal for iterative experimentation and model fine-tuning.

ClearML also offers powerful dataset version management capabilities that integrate seamlessly with YOLO26 training workflows. This feature allows you to:

To prepare your dataset for ClearML, follow these steps:

Upload your dataset using the ClearML Data tool:

This command will create a versioned dataset in ClearML that can be referenced in your training scripts, ensuring reproducibility and easy access to your data.

This guide has led you through the process of integrating ClearML with Ultralytics' YOLO26. Covering everything from initial setup to advanced model management, you've discovered how to leverage ClearML for efficient training, experiment tracking, and workflow optimization in your machine learning projects.

For further details on usage, visit ClearML's official YOLOv8 integration guide, which also applies to YOLO26 workflows.

Additionally, explore more integrations and capabilities of Ultralytics by visiting the Ultralytics integration guide page, which is a treasure trove of resources and insights.

Integrating Ultralytics YOLO26 with ClearML involves a series of steps to streamline your MLOps workflow. First, install the necessary packages:

Next, initialize the ClearML SDK in your environment using:

You then configure ClearML with your credentials from the ClearML Settings page. Detailed instructions on the entire setup process, including model selection and training configurations, can be found in our YOLO26 Model Training guide.

Using ClearML with Ultralytics YOLO26 enhances your machine learning projects by automating experiment tracking, streamlining workflows, and enabling robust model management. ClearML offers real-time metrics tracking, resource utilization monitoring, and a user-friendly interface for comparing experiments. These features help optimize your model's performance and make the development process more efficient. Learn more about the benefits and procedures in our MLOps Integration guide.

If you encounter issues during the integration of YOLO26 with ClearML, consult our Common Issues guide for solutions and tips. Typical problems might involve package installation errors, credential setup, or configuration issues. This guide provides step-by-step troubleshooting instructions to resolve these common issues efficiently.

Setting up a ClearML task for YOLO26 training involves initializing a task, selecting the model variant, loading the model, setting up training arguments, and finally, starting the model training. Here's a simplified example:

Refer to our Usage guide for a detailed breakdown of these steps.

After running your YOLO26 training script with ClearML, you can view the results on the ClearML results page. The output will include a URL link to the ClearML dashboard, where you can track metrics, compare experiments, and monitor resource usage. For more details on how to view and interpret the results, check our section on Viewing the ClearML Results Page.

**Examples:**

Example 1 (markdown):
```markdown
# Install the required packages for YOLO26 and ClearML
pip install ultralytics clearml
```

Example 2 (markdown):
```markdown
# Initialize your ClearML SDK setup process
clearml-init
```

Example 3 (swift):
```swift
from clearml import Task

from ultralytics import YOLO

# Step 1: Creating a ClearML Task
task = Task.init(project_name="my_project", task_name="my_yolo26_task")

# Step 2: Selecting the YOLO26 Model
model_variant = "yolo26n"
task.set_parameter("model_variant", model_variant)

# Step 3: Loading the YOLO26 Model
model = YOLO(f"{model_variant}.pt")

# Step 4: Setting Up Training Arguments
args = dict(data="coco8.yaml", epochs=16)
task.connect(args)

# Step 5: Initiating Model Training
results = model.train(**args)
```

Example 4 (unknown):
```unknown
clearml-agent daemon --queue QUEUES_TO_LISTEN_TO [--docker]
```

---

## Tutorial completi per Ultralytics YOLO

**URL:** https://docs.ultralytics.com/it/guides/

**Contents:**
- Tutorial completi per Ultralytics YOLO
- Guide
- Contribuisci alle nostre guide
- FAQ
  - Come posso addestrare un modello personalizzato di rilevamento oggetti utilizzando Ultralytics YOLO?
  - Quali metriche di performance dovrei usare per valutare il mio modello YOLO?
  - Perché dovrei usare Ultralytics Platform per i miei progetti di visione artificiale?
  - Quali sono i problemi comuni riscontrati durante l'addestramento del modello YOLO e come posso risolverli?
  - Come posso implementare il mio modello YOLO per il rilevamento di oggetti in tempo reale su dispositivi edge?
- Commenti

Benvenuti alle guide YOLO di Ultralytics. I nostri tutorial completi coprono vari aspetti del modello YOLO di rilevamento oggetti, dall'addestramento e previsione al deployment. Basato su PyTorch, YOLO si distingue per la sua eccezionale velocità e precisione nei compiti di rilevamento oggetti in tempo reale.

Che tu sia un principiante o un esperto di deep learning, i nostri tutorial offrono preziose intuizioni sull'implementazione e l'ottimizzazione di YOLO per i tuoi progetti di visione artificiale.

Guarda: Panoramica delle Guide Ultralytics YOLO26

Ecco una raccolta di guide approfondite per aiutarti a padroneggiare diversi aspetti di Ultralytics YOLO.

Accogliamo con favore i contributi della comunità! Se hai acquisito padronanza di un particolare aspetto di Ultralytics YOLO che non è ancora trattato nelle nostre guide, ti invitiamo a condividere la tua esperienza. Scrivere una guida è un ottimo modo per dare qualcosa in cambio alla comunità e aiutarci a rendere la nostra documentazione più completa e facile da usare.

Per iniziare, si prega di leggere la nostra Guida per i Contributori per le linee guida su come aprire una Pull Request (PR). Attendiamo con impazienza i vostri contributi.

Addestrare un modello personalizzato di rilevamento oggetti con Ultralytics YOLO è semplice. Inizia preparando il tuo dataset nel formato corretto e installando il pacchetto Ultralytics. Utilizza il seguente codice per avviare l'addestramento:

Per informazioni dettagliate sulla formattazione del dataset e opzioni aggiuntive, consulta la nostra guida Suggerimenti per l'addestramento del modello.

Valutare le prestazioni del tuo modello YOLO è fondamentale per comprenderne l'efficacia. Le metriche chiave includono la Mean Average Precision (mAP), l'Intersection over Union (IoU) e il punteggio F1. Queste metriche aiutano a valutare l'accuratezza e la precisione delle attività di object detection. Puoi saperne di più su queste metriche e su come migliorare il tuo modello nella nostra guida sulle YOLO Performance Metrics.

Ultralytics Platform è una piattaforma no-code che semplifica la gestione, l'addestramento e il deployment dei modelli YOLO. Supporta l'integrazione senza interruzioni, il tracking in tempo reale e l'addestramento nel cloud, rendendola ideale sia per i principianti che per i professionisti. Scopri di più sulle sue funzionalità e su come può ottimizzare il tuo flusso di lavoro con la nostra guida rapida a Ultralytics Platform.

I problemi comuni durante l'addestramento del modello YOLO includono errori di formattazione dei dati, mancate corrispondenze dell'architettura del modello e dati di addestramento insufficienti. Per risolvere questi problemi, assicurati che il tuo dataset sia formattato correttamente, verifica la presenza di versioni del modello compatibili e aumenta i tuoi dati di addestramento. Per un elenco completo di soluzioni, consulta la nostra guida Problemi comuni di YOLO.

La distribuzione di modelli YOLO su dispositivi edge come NVIDIA Jetson e Raspberry Pi richiede la conversione del modello in un formato compatibile come TensorRT o TFLite. Segui le nostre guide dettagliate per le distribuzioni NVIDIA Jetson e Raspberry Pi per iniziare con l'object detection in tempo reale su hardware edge. Queste guide ti guideranno attraverso l'installazione, la configurazione e l'ottimizzazione delle prestazioni.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

model = YOLO("yolo26n.pt")  # Load a pretrained YOLO model
model.train(data="path/to/dataset.yaml", epochs=50)  # Train on custom dataset
```

Example 2 (unknown):
```unknown
yolo task=detect mode=train model=yolo26n.pt data=path/to/dataset.yaml epochs=50
```

---

## Ultralytics Platform

**URL:** https://docs.ultralytics.com/it/platform/

**Contents:**
- Ultralytics Platform
- Cos'è la piattaforma Ultralytics?
- Flusso di lavoro: Dati → Addestramento → Distribuzione
- Infrastruttura Multi-Regione
- Caratteristiche principali
  - Preparazione dei Dati
  - Addestramento del Modello
  - Distribuzione
  - Gestione dell'Account
- Link Rapidi

Ultralytics Platform è una piattaforma di visione artificiale end-to-end completa che ottimizza l'intero flusso di lavoro ML, dalla preparazione dei dati alla distribuzione del modello. Progettata per team e individui che necessitano di soluzioni di visione artificiale pronte per la produzione senza la complessità dell'infrastruttura.

Guarda: Iniziare con la piattaforma Ultralytics

Ultralytics Platform è progettata per sostituire gli strumenti ML frammentati con una soluzione unificata. Combina le capacità di:

Piattaforma all-in-one con supporto nativo per YOLO11 YOLO26 e YOLO11 .

La Piattaforma segue un flusso di lavoro ottimizzato in tre fasi:

I tuoi dati rimangono nella tua regione. La Piattaforma Ultralytics gestisce l'infrastruttura in tre regioni globali:

Selezioni la tua regione durante l'onboarding, e tutti i tuoi dati, modelli e deployment rimangono in quella regione.

Inizia con queste risorse:

Per iniziare con Ultralytics Platform:

Per una guida dettagliata, consulta la pagina Quickstart.

Ultralytics Platform offre:

Ultralytics Platform supporta diversi tipi di GPU per l'addestramento in cloud:

Per informazioni complete sui prezzi e GPU , consultare la sezione Formazione sul cloud.

Puoi addestrare modelli ovunque e trasmettere le metriche alla Platform.

Requisiti di versione del pacchetto

L'integrazione della Piattaforma richiede Ultralytics>=8.4.0. Versioni precedenti NON funzioneranno con la Piattaforma.

Consulta Addestramento in Cloud per maggiori dettagli sull'addestramento remoto.

La Piattaforma include un editor di annotazioni completo che supporta:

Consulta Annotazione per la guida completa.

**Examples:**

Example 1 (php):
```php
graph LR
    subgraph Data["📁 Data"]
        A[Upload] --> B[Annotate]
        B --> C[Analyze]
    end
    subgraph Train["🚀 Train"]
        D[Configure] --> E[Train on GPU]
        E --> F[View Metrics]
    end
    subgraph Deploy["🌐 Deploy"]
        G[Test] --> H[Deploy Endpoint]
        H --> I[Monitor]
    end
    Data --> Train --> Deploy
```

Example 2 (unknown):
```unknown
pip install "ultralytics>=8.4.0"
```

Example 3 (markdown):
```markdown
# Set your API key
export ULTRALYTICS_API_KEY="your_api_key"

# Train with project/name to stream metrics
yolo train model=yolo26n.pt data=coco.yaml epochs=100 project=username/my-project name=exp1
```

---

## Validazione del modello con Ultralytics YOLO

**URL:** https://docs.ultralytics.com/it/modes/val/

**Contents:**
- Validazione del modello con Ultralytics YOLO
- Introduzione
- Perché convalidare con Ultralytics YOLO?
  - Funzionalità chiave della modalità Val
- Esempi di utilizzo
- Argomenti per la validazione del modello YOLO
  - Esempio di convalida con argomenti
- FAQ
  - Come valido il mio modello YOLO26 con Ultralytics?
  - Quali metriche posso ottenere dalla validazione del modello YOLO26?

La validazione è un passaggio critico nella pipeline di machine learning, che ti consente di valutare la qualità dei tuoi modelli addestrati. La modalità Val in Ultralytics YOLO26 fornisce una suite robusta di strumenti e metriche per valutare le prestazioni dei tuoi modelli di object detection. Questa guida serve come risorsa completa per capire come utilizzare efficacemente la modalità Val per garantire che i tuoi modelli siano sia accurati che affidabili.

Guarda: Tutorial sulle modalità di Ultralytics: Validazione

Ecco perché l'utilizzo della modalità Val di YOLO26 è vantaggioso:

Queste sono le funzionalità notevoli offerte dalla modalità Val di YOLO26:

Valida un modello YOLO26n addestrato accuratezza sul dataset COCO8. Non sono necessari argomenti poiché il model mantiene il suo training data e argomenti come attributi del modello. Consulta la sezione Argomenti di seguito per un elenco completo degli argomenti di validazione.

Errore di Multi-Processing di Windows

Su Windows, potresti ricevere un RuntimeError quando si avvia la convalida come script. Aggiungere un if __name__ == "__main__": prima del blocco del codice di convalida per risolverlo.

Durante la validazione dei modelli YOLO, è possibile ottimizzare diversi argomenti per ottimizzare il processo di valutazione. Questi argomenti controllano aspetti quali la dimensione dell'immagine di input, l'elaborazione batch e le soglie di performance. Di seguito è riportata un'analisi dettagliata di ciascun argomento per aiutarti a personalizzare efficacemente le impostazioni di validazione.

Ciascuna di queste impostazioni svolge un ruolo fondamentale nel processo di validazione, consentendo una valutazione personalizzabile ed efficiente dei modelli YOLO. La regolazione di questi parametri in base alle proprie esigenze e risorse specifiche può aiutare a raggiungere il miglior equilibrio tra accuratezza e performance.

Guarda: Come esportare i risultati della convalida del modello in CSV, JSON, SQL, DataFrame Polars e altro

Gli esempi seguenti mostrano la validazione del modello YOLO con argomenti personalizzati in Python e CLI.

Esporta ConfusionMatrix

Puoi anche salvare i risultati di ConfusionMatrix in diversi formati utilizzando il codice fornito.

Per maggiori dettagli, consultare la DataExportMixin documentazione della classe.

Per validare il tuo modello YOLO26, puoi utilizzare la modalità Val fornita da Ultralytics. Ad esempio, usando l'API python, puoi caricare un modello ed eseguire la validazione con:

In alternativa, puoi utilizzare l'interfaccia a riga di comando (CLI):

Per un'ulteriore personalizzazione, puoi modificare vari argomenti come imgsz, batch, e conf sia in modalità Python che CLI. Consulta la sezione Argomenti per la validazione del modello YOLO per l'elenco completo dei parametri.

La validazione del modello YOLO26 fornisce diverse metriche chiave per valutare le prestazioni del modello. Queste includono:

Utilizzando l'API Python, puoi accedere a queste metriche come segue:

Per una valutazione completa delle prestazioni, è fondamentale esaminare tutte queste metriche. Per maggiori dettagli, fare riferimento alle Caratteristiche principali della modalità Val.

L'utilizzo di Ultralytics YOLO per la validazione offre diversi vantaggi:

Questi vantaggi assicurano che i tuoi modelli siano valutati a fondo e possano essere ottimizzati per risultati superiori. Scopri di più su questi vantaggi nella sezione Perché convalidare con Ultralytics YOLO.

Sì, puoi validare il tuo modello YOLO26 usando un dataset personalizzato. Specifica l'argomento data l'argomento con il percorso del file di configurazione del dataset. Questo file deve includere il percorso del dati di validazione.

La validazione viene eseguita utilizzando i nomi delle classi del modello stesso, che è possibile visualizzare utilizzando model.names, e che potrebbero essere diversi da quelli specificati nel file di configurazione del set di dati.

Esempio usando la CLI:

Per opzioni più personalizzabili durante la convalida, consulta la sezione Esempio di convalida con argomenti.

Per salvare i risultati della convalida in un file JSON, puoi impostare il save_json a True durante l'esecuzione della convalida. Questo può essere fatto sia nell'API python che nella CLI.

Esempio usando la CLI:

Questa funzionalità è particolarmente utile per ulteriori analisi o integrazioni con altri strumenti. Consulta gli Argomenti per la convalida del modello YOLO per maggiori dettagli.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load an official model
model = YOLO("path/to/best.pt")  # load a custom model

# Validate the model
metrics = model.val()  # no arguments needed, dataset and settings remembered
metrics.box.map  # map50-95
metrics.box.map50  # map50
metrics.box.map75  # map75
metrics.box.maps  # a list containing mAP50-95 for each category
```

Example 2 (unknown):
```unknown
yolo detect val model=yolo26n.pt      # val official model
yolo detect val model=path/to/best.pt # val custom model
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")

# Customize validation settings
metrics = model.val(data="coco8.yaml", imgsz=640, batch=16, conf=0.25, iou=0.7, device="0")
```

Example 4 (unknown):
```unknown
yolo val model=yolo26n.pt data=coco8.yaml imgsz=640 batch=16 conf=0.25 iou=0.7 device=0
```

---

## Workouts Monitoring using Ultralytics YOLO26

**URL:** https://docs.ultralytics.com/guides/workouts-monitoring/

**Contents:**
- Workouts Monitoring using Ultralytics YOLO26
- Advantages of Workouts Monitoring
- Real World Applications
  - KeyPoints Map
  - AIGym Arguments
- FAQ
  - How do I monitor my workouts using Ultralytics YOLO26?
  - What are the benefits of using Ultralytics YOLO26 for workout monitoring?
  - How accurate is Ultralytics YOLO26 in detecting and tracking exercises?
  - Can I use Ultralytics YOLO26 for custom workout routines?

Monitoring workouts through pose estimation with Ultralytics YOLO26 enhances exercise assessment by accurately tracking key body landmarks and joints in real-time. This technology provides instant feedback on exercise form, tracks workout routines, and measures performance metrics, optimizing training sessions for users and trainers alike.

Watch: How to Monitor Workout Exercises with Ultralytics YOLO | Squats, Leg Extension, Pushups and More

Workouts Monitoring using Ultralytics YOLO

Here's a table with the AIGym arguments:

The AIGym solution also supports a range of object tracking parameters:

Additionally, the following visualization settings can be applied:

To monitor your workouts using Ultralytics YOLO26, you can utilize the pose estimation capabilities to track and analyze key body landmarks and joints in real-time. This allows you to receive instant feedback on your exercise form, count repetitions, and measure performance metrics. You can start by using the provided example code for push-ups, pull-ups, or ab workouts as shown:

For further customization and settings, you can refer to the AIGym section in the documentation.

Using Ultralytics YOLO26 for workout monitoring provides several key benefits:

You can watch a YouTube video demonstration to see these benefits in action.

Ultralytics YOLO26 is highly accurate in detecting and tracking exercises due to its state-of-the-art pose estimation capabilities. It can accurately track key body landmarks and joints, providing real-time feedback on exercise form and performance metrics. The model's pretrained weights and robust architecture ensure high precision and reliability. For real-world examples, check out the real-world applications section in the documentation, which showcases push-ups and pull-ups counting.

Yes, Ultralytics YOLO26 can be adapted for custom workout routines. The AIGym class supports different pose types such as pushup, pullup, and abworkout. You can specify keypoints and angles to detect specific exercises. Here is an example setup:

For more details on setting arguments, refer to the Arguments AIGym section. This flexibility allows you to monitor various exercises and customize routines based on your fitness goals.

To save the workout monitoring output, you can modify the code to include a video writer that saves the processed frames. Here's an example:

This setup writes the monitored video to an output file, allowing you to review your workout performance later or share it with trainers for additional feedback.

**Examples:**

Example 1 (markdown):
```markdown
# Run a workout example
yolo solutions workout show=True

# Pass a source video
yolo solutions workout source="path/to/video.mp4"

# Use keypoints for pushups
yolo solutions workout kpts="[6, 8, 10]"
```

Example 2 (python):
```python
import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("path/to/video.mp4")
assert cap.isOpened(), "Error reading video file"

# Video writer
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter("workouts_output.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Init AIGym
gym = solutions.AIGym(
    show=True,  # display the frame
    kpts=[6, 8, 10],  # keypoints for monitoring specific exercise, by default it's for pushup
    model="yolo26n-pose.pt",  # path to the YOLO26 pose estimation model file
    # line_width=2,  # adjust the line width for bounding boxes and text display
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()

    if not success:
        print("Video frame is empty or processing is complete.")
        break

    results = gym(im0)

    # print(results)  # access the output

    video_writer.write(results.plot_im)  # write the processed frame.

cap.release()
video_writer.release()
cv2.destroyAllWindows()  # destroy all opened windows
```

Example 3 (python):
```python
import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("path/to/video.mp4")
assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

gym = solutions.AIGym(
    line_width=2,
    show=True,
    kpts=[6, 8, 10],
)

while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or processing is complete.")
        break
    results = gym(im0)

cv2.destroyAllWindows()
```

Example 4 (python):
```python
from ultralytics import solutions

gym = solutions.AIGym(
    line_width=2,
    show=True,
    kpts=[6, 8, 10],  # For pushups - can be customized for other exercises
)
```

---

## YOLO Experiment Tracking and Visualization with Weights & Biases

**URL:** https://docs.ultralytics.com/integrations/weights-biases/

**Contents:**
- YOLO Experiment Tracking and Visualization with Weights & Biases
- Weights & Biases
- YOLO26 Training with Weights & Biases
- Installation
- Configuring Weights & Biases
- Usage: Training YOLO26 with Weights & Biases
  - W&B Arguments
  - Understanding the Output
  - Viewing the Weights & Biases Dashboard
- Key Features of the Weights & Biases Dashboard

Object detection models like Ultralytics YOLO26 have become integral to many computer vision applications. However, training, evaluating, and deploying these complex models introduce several challenges. Tracking key training metrics, comparing model variants, analyzing model behavior, and detecting issues require significant instrumentation and experiment management.

Watch: How to use Ultralytics YOLO26 with Weights and Biases

This guide showcases Ultralytics YOLO26 integration with Weights & Biases for enhanced experiment tracking, model-checkpointing, and visualization of model performance. It also includes instructions for setting up the integration, training, fine-tuning, and visualizing results using Weights & Biases' interactive features.

Weights & Biases is a cutting-edge MLOps platform designed for tracking, visualizing, and managing machine learning experiments. It features automatic logging of training metrics for full experiment reproducibility, an interactive UI for streamlined data analysis, and efficient model management tools for deploying across various environments.

You can use Weights & Biases to bring efficiency and automation to your YOLO26 training process. The integration allows you to track experiments, compare models, and make data-driven decisions to improve your computer vision projects.

To install the required packages, run:

For detailed instructions and best practices related to the installation process, be sure to check our YOLO26 Installation guide. While installing the required packages for YOLO26, if you encounter any difficulties, consult our Common Issues guide for solutions and tips.

After installing the necessary packages, the next step is to set up your Weights & Biases environment. This includes creating a Weights & Biases account and obtaining the necessary API key for a smooth connection between your development environment and the W&B platform.

Start by initializing the Weights & Biases environment in your workspace. You can do this by running the following command and following the prompted instructions.

Navigate to the Weights & Biases authorization page to create and retrieve your API key. Use this key when prompted to authenticate your environment with W&B.

Before diving into the usage instructions for YOLO26 model training with Weights & Biases, be sure to check out the range of YOLO26 models offered by Ultralytics. This will help you choose the most appropriate model for your project requirements.

Usage: Training YOLO26 with Weights & Biases

Enable or Disable Weights & Biases

If you want to enable or disable Weights & Biases logging in Ultralytics, you can use the yolo settings command. By default, Weights & Biases logging is disabled.

Upon running the usage code snippet above, you can expect the following key outputs:

After running the usage code snippet, you can access the Weights & Biases (W&B) dashboard through the provided link in the output. This dashboard offers a comprehensive view of your model's training process with YOLO26.

Real-Time Metrics Tracking: Observe metrics like loss, accuracy, and validation scores as they evolve during the training, offering immediate insights for model tuning. See how experiments are tracked using Weights & Biases.

Hyperparameter Optimization: Weights & Biases aids in fine-tuning critical parameters such as learning rate, batch size, and more, enhancing the performance of YOLO26. This helps you find the optimal configuration for your specific dataset and task.

Comparative Analysis: The platform allows side-by-side comparisons of different training runs, essential for assessing the impact of various model configurations and understanding which changes improve performance.

Visualization of Training Progress: Graphical representations of key metrics provide an intuitive understanding of the model's performance across epochs. See how Weights & Biases helps you visualize validation results.

Resource Monitoring: Keep track of CPU, GPU, and memory usage to optimize the efficiency of the training process and identify potential bottlenecks in your workflow.

Model Artifacts Management: Access and share model checkpoints, facilitating easy deployment and collaboration with team members on complex projects.

Viewing Inference Results with Image Overlay: Visualize the prediction results on images using interactive overlays in Weights & Biases, providing a clear and detailed view of model performance on real-world data. For more detailed information see Weights & Biases' image overlay capabilities.

By using these features, you can effectively track, analyze, and optimize your YOLO26 model's training, ensuring the best possible performance and efficiency for your object detection tasks.

This guide helped you explore the Ultralytics YOLO integration with Weights & Biases. It illustrates the ability of this integration to efficiently track and visualize model training and prediction results. By leveraging W&B's powerful features, you can streamline your machine learning workflow, make data-driven decisions, and improve your model's performance.

For further details on usage, visit Weights & Biases' official documentation or explore Soumik Rakshit's presentation from YOLO VISION 2023 on this integration.

Also, be sure to check out the Ultralytics integration guide page, to learn more about different exciting integrations like MLflow and Comet ML.

To integrate Weights & Biases with Ultralytics YOLO26:

Install the required packages:

Log in to your Weights & Biases account:

Train your YOLO26 model with W&B logging enabled:

This will automatically log metrics, hyperparameters, and model artifacts to your W&B project.

The key features include:

These features help in tracking experiments, optimizing models, and collaborating more effectively on YOLO26 projects.

After running your training script with W&B integration:

The dashboard offers insights into your model's training process, allowing you to analyze and improve your YOLO26 models effectively.

Yes, you can disable W&B logging using the following command:

To re-enable logging, use:

This allows you to control when you want to use W&B logging without modifying your training scripts.

Weights & Biases helps optimize YOLO26 models by:

These features help researchers and developers iterate faster and make data-driven decisions to improve their YOLO26 models.

**Examples:**

Example 1 (markdown):
```markdown
# Install the required packages for Ultralytics YOLO and Weights & Biases
pip install -U ultralytics wandb

# Enable W&B logging for Ultralytics
yolo settings wandb=True
```

Example 2 (markdown):
```markdown
import wandb

# Initialize your Weights & Biases environment
wandb.login(key="YOUR_API_KEY")
```

Example 3 (markdown):
```markdown
# Initialize your Weights & Biases environment
wandb login
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a YOLO model
model = YOLO("yolo26n.pt")

# Train and Fine-Tune the Model
model.train(data="coco8.yaml", epochs=5, project="ultralytics", name="yolo26n")
```

---
