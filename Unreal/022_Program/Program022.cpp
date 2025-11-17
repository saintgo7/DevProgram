// Blueprint Implementable

#include "Program022.h"

AProgram022::AProgram022()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram022::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Blueprint Implementable ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating blueprint implementable."));

    // Implement the program logic here...
}

void AProgram022::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
