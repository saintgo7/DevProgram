// Damage System

#include "Program041.h"

AProgram041::AProgram041()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram041::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Damage System ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating damage system."));

    // Implement the program logic here...
}

void AProgram041::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
