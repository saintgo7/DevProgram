// Input Action

#include "Program008.h"

AProgram008::AProgram008()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram008::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Input Action ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating input action."));

    // Implement the program logic here...
}

void AProgram008::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
