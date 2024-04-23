FROM python
WORKDIR /PremierLeagueTableApp
COPY . /PremierLeagueTableApp

RUN pip install httpx
RUN pip install colorama
RUN pip install tabulate

CMD ["python3", "PremierLeagueTableApp.py"]
