// EQS

#include "Program039.h"

AProgram039::AProgram039()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram039::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== EQS ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating eqs."));

    // Implement the program logic here...
}

void AProgram039::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
