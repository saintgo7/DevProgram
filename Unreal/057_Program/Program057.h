// Open Level
// Program 057

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program057.generated.h"

UCLASS()
class AProgram057 : public AActor
{
    GENERATED_BODY()

public:
    AProgram057();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
