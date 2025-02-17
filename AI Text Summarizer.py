from transformers import pipeline

def summarize_text(text,max_length=50):
    summarizer = pipeline('summarization', model='t5-small')
    summary = summarizer(text, max_length=max_length, min_length= 20, do_sample=False)
    return summary[0]['summary_text']

if __name__ == '__main__':
    long_text = """
        Artificial Intelligence (AI) is transforming industries by automating tasks, enhancing decision-making, 
        and creating new opportunities. AI models such as machine learning and deep learning allow computers to 
        recognize patterns, make predictions, and improve over time. AI is being widely used in healthcare, 
        finance, and technology sectors. Companies are leveraging AI to optimize operations, enhance customer 
        experiences, and drive innovation. However, ethical concerns such as bias, job displacement, and 
        privacy issues remain significant challenges that need to be addressed for AI to be more beneficial to society.
    """
    
    summary_result = summarize_text(long_text)
    print('Summary \n ', summary_result)