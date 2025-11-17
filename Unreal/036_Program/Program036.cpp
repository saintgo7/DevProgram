// AI Controller

#include "Program036.h"

AProgram036::AProgram036()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram036::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== AI Controller ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating ai controller."));

    // Implement the program logic here...
}

void AProgram036::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
