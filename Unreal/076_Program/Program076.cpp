// Sound

#include "Program076.h"

AProgram076::AProgram076()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram076::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Sound ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating sound."));

    // Implement the program logic here...
}

void AProgram076::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
