# PDF Analyzer

1. Upload PDF
2. [Extract text](https://www.geeksforgeeks.org/extract-text-from-pdf-file-using-python/)
3. [Translate](https://huggingface.co/models?pipeline_tag=translation&sort=downloads) if needed
4. Use GPT to get data values
5. Return as JSON

## Example

    % python3 app.py

    Pages: 139
    Length: 510661

    Finding “scope”:
    ———————————————————————
    Scope 1 Scope 2 Scope 3
    scope 3 för att skapa en bättre bild av koncernens totala klimatpåverkan – den 
    utsläpp inom scope 1, 2 och delar av scope 3. 
    i scope 3. Till dessa hör inte minst utsläpp relate ­
    byggnads- och förbrukningsmaterial)Utsläpp inom scope 3 som i dags läget inte 
    inkluderas i ICA Gruppens netto noll-målUtsläpp inom scope 3 som i dags läget inte 
    minska klimatpåverkan. Matsvinn såväl som klimatavtrycket från det ICA säljer ingår även till viss del i scope 3, dvs områden där ICA har 
    indirekt påverkan. Under året initierades en kartläggning av de olika delströmmarna i scope 3 för att skapa en bättre bild av ICAs totala 
    genomlysning av koncernens utsläpp inom scope 3, för att 
    Scope 1, scope 2 och, om så är lämpligt, scope 3 utsläpp av växthusgaser (green­
    Direkta utsläpp av växthusgaser enligt Scope 1 14 428 17 649 26 724
    Indirekta utsläpp av växthusgaser enligt Scope 2 2 919 2 907 27 341
    Indirekta utsläpp av växthusgaser enligt Scope 3 61 444 71 565 74 447
    Scope 1,/uni00A018%
    Scope 2,/uni00A04%
    Scope 3, /uni00A078%
    resor (Scope 1, 2 och delar av Scope 3). Både den svenska 
    tive scope:
    • Scope 1: Utsläpp från köldmedia i lager och i av ICA 
    • Scope 2: Utsläpp från energi i lager samt i av ICA 
    • Scope 3: Utsläpp från tjänsteresor, utsläpp från svenska 
    • Fossila bränslen beräknas enligt Scope 1 och förnybara 
    bränslen enligt Scope 1 och 3.
    faktorer från GHG Protokollets verktyg ”Scope 3 Evaluator” 
    ———————————————————————

## ChatGPT

	I want to build an AI/ML tool that:
	
	1. Can read a PDF with company’s annual report
	2. Can analyse the PDF and extract values for Scope 1, 2 and 3 of Carbon Emissions
	3. Display the values in a table
	
	Describe how to build this tool, step by step.

Building an AI/ML tool for extracting and displaying carbon emissions data from a company's annual report involves several stages. Here's a step-by-step guide to help you develop such a tool:

Gather data:
Collect a large dataset of annual reports in PDF format. Ideally, these reports should come from diverse industries and contain information about Scope 1, 2, and 3 carbon emissions.

Preprocess the data:
Convert the PDFs into machine-readable text. You can use libraries like PyPDF2, pdfrw, or pdfminer.six for this task. Perform additional preprocessing like removing special characters, stop words, and other noise.

Label the data:
Manually annotate a subset of the dataset with relevant labels for Scope 1, 2, and 3 carbon emissions. This labeled data will be used for training and validation purposes.

Train a Named Entity Recognition (NER) model:
Using the labeled data, train a Named Entity Recognition (NER) model to identify and extract Scope 1, 2, and 3 carbon emissions information. You can use pre-trained models like BERT, RoBERTa, or other transformer-based models available in the Hugging Face library. Fine-tune the model on your labeled data.

Develop a table extraction algorithm:
Design an algorithm to process the extracted text and identify relevant tables containing carbon emissions data. You can use heuristic approaches, regex patterns, or machine learning techniques like deep learning-based table detection.

Post-processing and data validation:
After extracting the relevant tables, perform post-processing to clean and validate the extracted data, ensuring accuracy and consistency.

Build the user interface:
Create a user-friendly interface where users can upload a PDF file and view the extracted carbon emissions data in a table format. You can use web development frameworks like Flask or Django for the backend and React, Angular, or Vue.js for the frontend.

Integrate the components:
Connect the NER model, table extraction algorithm, and user interface, ensuring seamless integration and functionality.

Test the tool:
Perform thorough testing of the tool to identify and fix any issues or inaccuracies. This should include testing with a variety of annual reports from different industries and sources.

Deploy and monitor:
Deploy the tool on a server or cloud platform, and monitor its performance. Make sure to regularly update and maintain the tool, fine-tuning the NER model and improving the table extraction algorithm as needed.
