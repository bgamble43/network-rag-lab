import argparse
from rag_engine import build_rag_chain

def main():
    parser = argparse.ArgumentParser(description="Ask Cisco routing questions.")
    parser.add_argument("question", type=str, help="Your question in quotes")
    args = parser.parse_args()

    qa = build_rag_chain()
    result = qa.invoke(args.question)

    print("\n📌 Answer:\n" + result["result"])
    print("\n📚 Source Files:")
    for doc in result["source_documents"]:
        print(f"- {doc.metadata.get('source')}")

if __name__ == "__main__":
    main()
