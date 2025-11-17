// AI Controller
// Program 036

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program036.generated.h"

UCLASS()
class AProgram036 : public AActor
{
    GENERATED_BODY()

public:
    AProgram036();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
