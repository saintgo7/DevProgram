// Hit Result

#include "Program090.h"

AProgram090::AProgram090()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram090::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Hit Result ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating hit result."));

    // Implement the program logic here...
}

void AProgram090::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
