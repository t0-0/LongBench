import json
import csv
import argparse


def json_to_csv(input_file, output_file):
    with open(input_file, "r") as json_file:
        data = json.load(json_file)

    with open(output_file, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)

        order = [
            "narrativeqa",
            "qasper",
            "multifieldqa_en",
            "multifieldqa_zh",
            "hotpotqa",
            "2wikimqa",
            "musique",
            "dureader",
            "gov_report",
            "qmsum",
            "multi_news",
            "vcsum",
            "trec",
            "triviaqa",
            "samsum",
            "lsht",
            "passage_count",
            "passage_retrieval_en",
            "passage_retrieval_zh",
            "lcc",
            "repobench-p",
        ]
        # writer.writerow(order)

        row = [data.get(key, "") for key in order]
        writer.writerow(row)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--file_name",
        type=str,
        default=None,
    )
    args = parser.parse_args()
    json_to_csv(args.file_name + ".json", args.file_name + ".csv")
