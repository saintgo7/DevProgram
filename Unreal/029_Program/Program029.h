// Timer Handle
// Program 029

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program029.generated.h"

UCLASS()
class AProgram029 : public AActor
{
    GENERATED_BODY()

public:
    AProgram029();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
