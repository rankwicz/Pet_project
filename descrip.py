def initial_data_check(df, name='DataFrame'):
    print(f"\n--- 📊 Информация о {name} ---\n")
    print("✅ Размерность:", df.shape)
    
    print("\n🔍 Первые 5 строк:")
    print(df.head())
    
    print("\n🧩 Пропуски в данных:")
    print(df.isnull().sum())
    
    print("\n📈 Описательная статистика:")
    print(df.describe(include='all'))
    
    print("\n🗺️ Типы данных:")
    print(df.dtypes)
    
    print("\n📋 Уникальные значения в каждом столбце:")
    for col in df.columns:
        print(f"{col}: {df[col].nunique()} уникальных значений")