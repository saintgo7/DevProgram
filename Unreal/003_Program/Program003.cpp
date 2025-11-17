// Pawn

#include "Program003.h"

AProgram003::AProgram003()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram003::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Pawn ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating pawn."));

    // Implement the program logic here...
}

void AProgram003::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
