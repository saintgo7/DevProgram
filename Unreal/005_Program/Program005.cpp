// Player Controller

#include "Program005.h"

AProgram005::AProgram005()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram005::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Player Controller ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating player controller."));

    // Implement the program logic here...
}

void AProgram005::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
