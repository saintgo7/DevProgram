// Timer Manager

#include "Program030.h"

AProgram030::AProgram030()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram030::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Timer Manager ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating timer manager."));

    // Implement the program logic here...
}

void AProgram030::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
