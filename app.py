# # import sqlite3 # kad galetumem dirbti su sqlite

# # conn = sqlite3.connect("Darbuotojai.db") # kaip greitkeli 

# # cur = conn.cursor() # automobilis, kuris tuo keliu vazineja pasikroves duomenimis

# # # cur.execute("""
# # #             INSERT INTO DARBUOTOJAS(ASMENSKODAS, VARDAS, PAVARDE, GIMIMOMETAI, PAREIGOS, SKYRIUS_PAVADINIMAS)
# # #             VALUES ("39810100106", "Juozas", "Juozaitis", "1998-10-10", "Testuotojas", "Testavimo");
# # #             """) # tarsi pakrauna duomenis i automobili
# # # conn.commit() # jau vaziuok


# # # cur.execute("Select * From Darbuotojas")
# # # rows = cur.fetchall() # vaziuok, bet sikart su tikslu parsivezti

# # # for row in rows:
# # #     # print(row)
# # #     # rows yra sarasas tuplu [(row),(row),(row)]
# # #     # row (asmens_kodas,vardas,pavarde,isidarbinimometai)
# # #     print(row)

# # def gauti_darbuotojus(cursor):
# #     cursor.execute("Select * From Darbuotojas Where age > {user_input}")
# #     rows = cursor.fetchall() # vaziuok, bet sikart su tikslu parsivezti
# #     return rows


# # for row in gauti_darbuotojus(cur):
# #     print(row)


# # conn.close()

# # import sqlite3 # kad galetumem dirbti su sqlite

# # conn = sqlite3.connect("Darbuotojai.db") # kaip greitkeli 

# # cur = conn.cursor() # automobilis, kuris tuo keliu vazineja pasikroves duomenimis

# # with conn: 
# #     cur.execute("""
# #                 INSERT INTO DARBUOTOJAS(ASMENSKODAS, VARDAS, PAVARDE, GIMIMOMETAI, PAREIGOS, SKYRIUS_PAVADINIMAS)
# #                 VALUES ("39810100107", "Juozas", "Juozaitis", "1998-10-10", "Testuotojas", "Testavimo");
# #                 """) # tarsi pakrauna duomenis i automobili


# # cur.execute(Update Users Set Name = ? Where Id = ?, ("Jonas",17))
# # kint = (15)

# # cur.execute(Update Users Set Name = :vardas Where Id = :idelis, {"idelis":17,"vardas":"Mantas"})

# # import sqlite3 # kad galetumem dirbti su sqlite

# # conn = sqlite3.connect("Darbuotojai.db") # kaip greitkeli 

# # cur = conn.cursor() # automobilis, kuris tuo keliu vazineja pasikroves duomenimis

# # # cur.execute("""
# # #             INSERT INTO DARBUOTOJAS(ASMENSKODAS, VARDAS, PAVARDE, GIMIMOMETAI, PAREIGOS, SKYRIUS_PAVADINIMAS)
# # #             VALUES ("39810100106", "Juozas", "Juozaitis", "1998-10-10", "Testuotojas", "Testavimo");
# # #             """) # tarsi pakrauna duomenis i automobili
# # # conn.commit() # jau vaziuok

# # with conn:
# #     cur.execute("Select * From Darbuotojas")
# #     rows = cur.fetchall() # vaziuok, bet sikart su tikslu parsivezti
# #     for row in rows:
# #         print(row)  
         
# # cur.execute("Select * From Darbuotojas")
# # rows = cur.fetchall() # vaziuok, bet sikart su tikslu parsivezti
# # for row in rows:
# #     print(row)  


# import pymysql # 1. Pakeitėme biblioteką iš sqlite3

# # 2. Prisijungimas: MySQL reikia adreso, vartotojo ir slaptažodžio
# conn = pymysql.connect(
#     host="localhost",       # Dažniausiai localhost
#     port=3306,
#     user="Justas",            # Jūsų MySQL vartotojas
#     password="Code2024.",    # Jūsų MySQL slaptažodis
#     database="studentu_pav"     # Duomenų bazės pavadinimas (turi egzistuoti)
# )

# cur = conn.cursor() # 'Automobilis' veikia taip pat

# # Dėmesio: MySQL kabutėms geriau naudoti viengubas (')
# # cur.execute("""
# #     INSERT INTO DARBUOTOJAS(ASMENSKODAS, VARDAS, PAVARDE, GIMIMOMETAI, PAREIGOS, SKYRIUS_PAVADINIMAS)
# #     VALUES ('39810100106', 'Juozas', 'Juozaitis', '1998-10-10', 'Testuotojas', 'Testavimo');
# # """)
# # conn.commit() # Visada reikia 'commit', kai įrašome duomenis

# # SELECT operacija
# try:
#     cur.execute("SELECT * FROM DARBUOTOJAS")
#     rows = cur.fetchall() # 'Parsivežame' duomenis
#     for row in rows:
#         print(row)

# finally:
#     # 3. MySQL svarbu uždaryti ryšį, kad neužkimštumėte serverio
#     conn.close()


# import os
# from typing import Optional
# from dotenv import load_dotenv
# from sqlalchemy import create_engine, String 
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# load_dotenv()

# db_user = os.getenv("DB_USER", "Justas")
# db_pass = os.getenv("DB_PASS", "Code2024.")
# db_host = os.getenv("DB_HOST", "localhost")
# db_name = os.getenv("DB_NAME", "darbine")

# # 2. DRIVER: Explicitly use a driver like pymysql (pip install pymysql)
# connection_string = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}"

# engine = create_engine(connection_string)

# class Base(DeclarativeBase):
#     pass

# class Person(Base):
#     __tablename__ = 'People'
    
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     name: Mapped[str] = mapped_column(String(50)) 
#     last_name: Mapped[Optional[str]] = mapped_column(String(50))
#     age: Mapped[Optional[int]]

# class Car(Base):
#     __tablename__ = 'Cars'
    
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     make: Mapped[str] = mapped_column(String(50))
#     model: Mapped[Optional[str]] = mapped_column(String(50))
#     year: Mapped[Optional[int]]

# Base.metadata.create_all(engine)



# from sqlalchemy import create_engine, String 
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# db_user = "Justas"
# db_pass = "Code2024."
# db_host = "localhost"
# db_name = "aiu6"

# # 2. DRIVER: Explicitly use a driver like pymysql (pip install pymysql)
# connection_string = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}"

# engine = create_engine(connection_string) # sukuriam greitkeli (arciausiai)

# class Base(DeclarativeBase): # sqlalchemy reikalauja, kad butu bazine klase, kuria visos kitos
#     pass

# class Person(Base): # paveldi Base, dėl to kad butu atpažinta kaip lentele
#     __tablename__ = 'people' # nurodom lenteles pavadinima duomenu bazeje

#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     name = mapped_column(String(50)) 
#     last_name = mapped_column(String(50))
#     age : Mapped[int]

# class Car(Base):
#     __tablename__ = 'cars'
#     id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     make = mapped_column(String(50))
#     model = mapped_column(String(50))
#     year: Mapped[int]

# Base.metadata.create_all(engine) # Create table if not exists



# import os
# from typing import Optional
# from dotenv import load_dotenv
# from sqlalchemy import create_engine, String, select
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

# load_dotenv()

# db_user = os.getenv("DB_USER")
# db_pass = os.getenv("DB_PASS")
# db_host = os.getenv("DB_HOST")
# db_name = os.getenv("DB_NAME")

# # 2. DRIVER: Explicitly use a driver like pymysql (pip install pymysql)
# connection_string = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}"

# engine = create_engine(connection_string)

# class Base(DeclarativeBase):
#     pass

# class Person(Base):
#     __tablename__ = 'People'
    
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     name: Mapped[str] = mapped_column(String(50)) 
#     last_name: Mapped[Optional[str]] = mapped_column(String(50))
#     age: Mapped[Optional[int]]

#     def __init__(self, name,last_name,age):
#         self.name = name
#         self.last_name = last_name
#         self.age = age

#     def __str__(self):
#         return f"{self.name}, {self.last_name}"

# class Car(Base):
#     __tablename__ = 'Cars'
    
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     make: Mapped[str] = mapped_column(String(50))
#     model: Mapped[Optional[str]] = mapped_column(String(50))
#     year: Mapped[Optional[int]]

# Base.metadata.create_all(engine)

# # sessionmaker - automobiliu gamykla

# session_maker = sessionmaker(engine)

# # def add_person(sm,vardas,pavarde,amzius):

# #     with sm() as session: # session kaip sukurtas automobilis (kaip cursor)
# #         zmogus = Person(name=vardas,last_name=pavarde,age=amzius)
# #         session.add(zmogus)
# #         session.commit()

# # def get_person_by_id(sm,id):
# #     with sm() as session:
# #         person = session.get(Person,id)
# #     return person


# def add_person(sm,vardas,pavarde,amzius):

#     with sm() as session: # session kaip sukurtas automobilis (kaip cursor)
#         zmogus = Person(vardas,pavarde,amzius)
#         session.add(zmogus)
#         session.commit()

# def get_people_list(sm):
#     with sm() as session:
#         stmt = select(Person)
#         # stmt = select(Person).filter_by(name="Jonas")
#         people = session.execute(stmt).scalars().all()
#     return people

# def get_person_by_id(session,id):
#     person = session.get(Person,id)
#     return person

# def update_person(sm,id):
#     # zmogus = get_person_by_id(sm,id)
#     # print(zmogus)
#     with sm() as session:
#         person = get_person_by_id(session,id)
#         person.name = "Naujas2"
#         session.commit()

# def delete_person(sm,id):
#     # zmogus = get_person_by_id(sm,id)
#     # print(zmogus)
#     with sm() as session:
#         person = get_person_by_id(session,id)
#         if person: # patikrina ar person nėra None
#             session.delete(person)
#             session.commit()
# # update_person(session_maker,1)
# # delete_person(session_maker,1)

# # peeps = get_people_list(session_maker)
# # # print(get_person_by_id(session_maker,2))
# # for person in peeps:
# #     print(person)



# # with session_maker() as session:
# #         stmt = select(Person)
# #         people = session.execute(stmt).scalars().all()
# #         people = session.execute(stmt).scalar_one()
# #         people = session.execute(stmt).one_or_none() # jeigu daugiau nei vienas, mes klaida
# #         people = session.execute(stmt).fetchall()
# #         session.delete()
# #         session.close()
# add_person(session_maker,"Mantas","Muntaitis",39)





import os
from typing import Optional, List
from dotenv import load_dotenv
from sqlalchemy import create_engine, String, select, Engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

load_dotenv()

# Konfigūracija
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

connection_string = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
engine = create_engine(connection_string)

class Base(DeclarativeBase):
    pass

class Person(Base):
    __tablename__ = 'People'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50)) 
    last_name: Mapped[Optional[str]] = mapped_column(String(50))
    age: Mapped[Optional[int]]

    def __repr__(self) -> str:
        return f"Person(id={self.id}, name={self.name}, last_name={self.last_name}, age={self.age})"

# Sukuriamos lentelės
Base.metadata.create_all(engine)

# --- FUNKCIJOS ---

def add_person(engine: Engine, vardas: str, pavarde: str, amzius: int):
    with Session(engine) as session:
        zmogus = Person(name=vardas, last_name=pavarde, age=amzius)
        session.add(zmogus)
        session.commit()
        print("Vartotojas pridėtas!")

def get_people_list(engine: Engine) -> List[Person]:
    with Session(engine) as session:
        stmt = select(Person)
        people = session.execute(stmt).scalars().all()
        return list(people)

def update_person_name(engine: Engine, p_id: int, naujas_vardas: str):
    with Session(engine) as session:
        person = session.get(Person, p_id)
        if person:
            person.name = naujas_vardas
            session.commit()
            print("Duomenys atnaujinti.")
        else:
            print("Vartotojas nerastas.")

def delete_person(engine: Engine, p_id: int):
    with Session(engine) as session:
        person = session.get(Person, p_id)
        if person:
            session.delete(person)
            session.commit()
            print("Vartotojas ištrintas.")
        else:
            print("Klaida: Vartotojas nerastas.")

# --- PAGRINDINIS CIKLAS ---

def main():
    while True:
        print("\n--- PASIRINKITE VEIKSMĄ ---")
        print("1. Rodyti visus žmones")
        print("2. Pridėti žmogų")
        print("3. Atnaujinti vardą")
        print("4. Ištrinti žmogų")
        print("5. Išeiti")
        
        pasirinkimas = input("Įveskite numerį: ")

        if pasirinkimas == "1":
            zmones = get_people_list(engine)
            for z in zmones:
                print(z)

        elif pasirinkimas == "2":
            v = input("Vardas: ")
            p = input("Pavardė: ")
            a = int(input("Amžius: "))
            add_person(engine, v, p, a)

        elif pasirinkimas == "3":
            idx = int(input("Įveskite ID, kurį norite keisti: "))
            n_vardas = input("Įveskite naują vardą: ")
            update_person_name(engine, idx, n_vardas)

        elif pasirinkimas == "4":
            idx = int(input("Įveskite ID ištrynimui: "))
            delete_person(engine, idx)

        elif pasirinkimas == "5":
            print("Viso gero!")
            break
        else:
            print("Neteisingas pasirinkimas.")

if __name__ == "__main__":
    main()