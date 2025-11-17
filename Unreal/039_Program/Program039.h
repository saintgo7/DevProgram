// EQS
// Program 039

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program039.generated.h"

UCLASS()
class AProgram039 : public AActor
{
    GENERATED_BODY()

public:
    AProgram039();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
