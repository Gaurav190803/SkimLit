from sklearn.metrics import accuracy_score, precision_recall_fscore_support


def get_lines(filename):
    """  
    input - filename
    output- file text as a list
    """
    with open(filename,"r") as f:
        return f.readlines()
    

def preprocess_text_with_line_number(filename):
    """
    returns list of dict of abstracts

    """
    input_lines = get_lines(filename)

    abstract_lines = ""
    abstract_samples = []

    for line in input_lines:
        if(line.startswith("###")):
            abstract_id = line
            abstract_lines = ""

        elif(line.isspace()):
            abstract_line_split = abstract_lines.splitlines()

            for abstract_line_num,abstract_line in enumerate(abstract_line_split):
                line_data = {}
                target_text_split = abstract_line.split("\t")
                line_data["target"] = target_text_split[0]
                line_data["text"] = target_text_split[1].lower()
                line_data["line_num"] = abstract_line_num
                line_data["total_lines"] = len(abstract_line_split)-1
                abstract_samples.append(line_data)

        else:
            abstract_lines += line

    return abstract_samples

def calculate_results(y_true, y_pred):

  # Calculate model accuracy
  model_accuracy = accuracy_score(y_true, y_pred) * 100
  # Calculate model precision, recall and f1 score using "weighted average
  model_precision, model_recall, model_f1, _ = precision_recall_fscore_support(y_true, y_pred, average="weighted")
  model_results = {"accuracy": model_accuracy,
                  "precision": model_precision,
                  "recall": model_recall,
                  "f1": model_f1}
  return model_results