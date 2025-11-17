// Overlap

#include "Program089.h"

AProgram089::AProgram089()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram089::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Overlap ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating overlap."));

    // Implement the program logic here...
}

void AProgram089::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
