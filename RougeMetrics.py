from rouge import Rouge

if __name__ == '__main__':
    "https://towardsdatascience.com/the-ultimate-performance-metric-in-nlp-111df6c64460"
    model_out = [
        "he began by starting a five person war cabinet and included chamberlain as lord president of the council",
        "the siege lasted from 250 to 241 bc, the romans laid siege to lilybaeum",
        "the original ocean water was found in aquaculture"]

    reference = [
        "he began his premiership by forming a five-man war cabinet which included chamberlain as lord president of the council",
        "the siege of lilybaeum lasted from 250 to 241 bc, as the roman army laid siege to the carthaginian-held sicilian city of lilybaeum",
        "the original mission was for research into the uses of deep ocean"]
    rouge = Rouge()

    scores = rouge.get_scores(model_out, reference, avg=True)

    print(scores)