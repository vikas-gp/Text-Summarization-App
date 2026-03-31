import csv
from rouge_score import rouge_scorer
from nltk.translate.bleu_score import sentence_bleu

def evaluate_summary(reference, generated):

    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2','rougeL'], use_stemmer=True)
    rouge_scores = scorer.score(reference, generated)

    reference_tokens = [reference.split()]
    generated_tokens = generated.split()

    bleu_score = sentence_bleu(reference_tokens, generated_tokens)

    return {
        "ROUGE-1":rouge_scores['rouge1'].fmeasure,
        "ROUGE-2":rouge_scores['rouge2'].fmeasure,
        "ROUGE-L":rouge_scores['rougeL'].fmeasure,
        "BLEU" : bleu_score
    }

def save_results(reference, generated, scores, filename="results.csv"):

    file_exists = False

    try:
        with open(filename, "r"):
            file_exists = True
    except FileNotFoundError:
        pass

    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Write header only once
        if not file_exists:
            writer.writerow([
                "Reference",
                "Generated",
                "ROUGE-1",
                "ROUGE-2",
                "ROUGE-L",
                "BLEU"
            ])

        writer.writerow([
            reference,
            generated,
            scores["ROUGE-1"],
            scores["ROUGE-2"],
            scores["ROUGE-L"],
            scores["BLEU"]
        ])

if __name__ == "__main__":
    reference = "Born in Mashhad to the Khamenei family, he studied at a hawza there before settling in Qom in 1958, where he attended the classes of Ruhollah Khomeini. Khamenei became involved in opposition to Shah Mohammad Reza Pahlavi, and was arrested six times before being exiled for three years by Pahlavi's regime. Khamenei was a mainstream figure in the Iranian Revolution, and upon its success, held many posts in the newly established Islamic republic. In the aftermath of the revolution, he was the target of an attempted assassination that paralysed his right arm. Khamenei served as the third president of Iran from 1981 to 1989 during the Iran–Iraq War, when he also developed close ties to the Islamic Revolutionary Guard Corps (IRGC). After the death and state funeral of Ruhollah Khomeini in 1989, Khamenei was elected supreme leader by the Assembly of Experts. During the deliberations, Khamenei expressed reservations about his religious qualifications and suitability for the position, as he was a mid-ranking cleric and did not meet the constitutional requirement of marja'. The constitution was subsequently amended to remove that requirement, and the Assembly reconfirmed his leadership later that year."
    generated = "Born in Mashhad to the Khamenei family, he studied at a hawza in Qom. Became involved in opposition to Shah Mohammad Reza Pahlavi, and was arrested six times. Was exiled for three years by the regime. Was the target of an attempted assassination that paralysed his right arm. Was elected supreme leader by the Assembly of Experts in 1989."

    scores = evaluate_summary(reference, generated)

    print('Scores:',scores)


    save_results(reference, generated, scores)

    print("Results saved to results.csv")